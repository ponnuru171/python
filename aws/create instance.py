import boto3
import boto.ec2
import os
from operator import itemgetter
import time
# variables
aws_region = "us-east-2"
aws_az1 = "us-east-2a"
aws_az2 = "us-east-2b"
vpc_cidr = "10.100.0.0/16"
public_subnet_cidr = "10.100.1.0/24"
private_subnet_cidr = "10.100.2.0/24"
source_cidr = '0.0.0.0/0'
user_data_content = """#!/bin/bash
sudo yum update -y
sudo yum install -y httpd
sudo yum -y install mariadb-server
sudo systemctl start httpd"""

# initialize boto3 ec2 client and resource
ec2_resource = boto3.resource('ec2', aws_region)
ec2_client = boto3.client('ec2', aws_region)

# create a vpc
vpc = ec2_resource.create_vpc(CidrBlock=vpc_cidr)
vpc.wait_until_available()
print('VPC created successfully with VPC ID: ' + vpc.id)

# modify vpc to enable dns hostname
vpc.modify_attribute(EnableDnsHostnames={'Value':True})

# create public subnet
public_subnet = vpc.create_subnet(AvailabilityZone=aws_az1,CidrBlock=public_subnet_cidr)
ec2_client.modify_subnet_attribute(MapPublicIpOnLaunch={'Value': True},SubnetId=public_subnet.id)
print('Public Subnet created successfully with SUBNET ID: ' + public_subnet.id)

# create a private subnet
private_subnet = vpc.create_subnet(AvailabilityZone=aws_az2,CidrBlock=private_subnet_cidr)
print('Private Subnet created successfully with SUBNET ID: ' + private_subnet.id)

# create an internet gateway and attach to the vpc
internet_gateway = ec2_resource.create_internet_gateway()
internet_gateway.attach_to_vpc(VpcId=vpc.id)
print('Internet Gateway created successfully with GATEWAY ID: ' + internet_gateway.id)

# create a public route table and assosiate to public subnet
public_route_table = ec2_resource.create_route_table(VpcId=vpc.id)
public_route_table.associate_with_subnet(SubnetId=public_subnet.id )
# create route to Internet Gateway in public route table
public_route = ec2_client.create_route(RouteTableId=public_route_table.id,DestinationCidrBlock=source_cidr,GatewayId=internet_gateway.id)
print('Public Route Table with ID ' + public_route_table.id + ' created successfully')

# create a private route table and assosiate to private subnet
private_route_table = ec2_resource.create_route_table(VpcId=vpc.id)
private_route_table.associate_with_subnet(SubnetId=private_subnet.id)
print('Private Route Table with ID ' + private_route_table.id + ' created successfully')

# create a security group
security_group = ec2_resource.create_security_group(GroupName='myvpc_security_group',Description='Used by LAMP',VpcId= vpc.id)

# create ssh and http ingress rules
ec2_client.authorize_security_group_ingress(GroupId=security_group.id,IpProtocol='tcp',FromPort=22,ToPort=22,CidrIp=source_cidr)
ec2_client.authorize_security_group_ingress(GroupId=security_group.id,IpProtocol='tcp',FromPort=80,ToPort=80,CidrIp=source_cidr)
print('Security Group with ID ' + security_group.id + ' created successfully')

# get the latest AMI ID for Amazon Linux 2
ec2_ami_ids = ec2_client.describe_images(
    Filters=[{'Name':'name','Values':['amzn2-ami-hvm-2.0.????????-x86_64-gp2']},{'Name':'state','Values':['available']}],
    Owners=['amazon'])
image_details = sorted(ec2_ami_ids['Images'],key=itemgetter('CreationDate'),reverse=True)
ec2_ami_id = image_details[0]['ImageId']

# create a key pair
outfile = open('my_keypair.pem','w')
keypair = ec2_client.create_key_pair(KeyName='my_keypair')
keyval = keypair['KeyMaterial']
outfile.write(keyval)
outfile.close()
os.chmod('my_keypair.pem', 400)
print('Key Pair my_keypair created successfully')

# create an ec2 instance
ec2_instance = ec2_resource.create_instances(
    ImageId=ec2_ami_id,
    InstanceType='t2.micro',
    KeyName='my_keypair',
    Monitoring={'Enabled':False},
    SecurityGroupIds=[security_group.id],
    SubnetId=public_subnet.id,
    UserData=user_data_content,
    MaxCount=1,
    MinCount=1,
    PrivateIpAddress='10.100.1.10')
ec2_instance_id = ec2_instance[0].id
print('Creating EC2 instance')

#wait untill the ec2 is running
waiter = ec2_client.get_waiter('instance_running')
waiter.wait(InstanceIds=[ec2_instance_id])
print('EC2 Instance created successfully with ID: ' + ec2_instance_id)

# create tags
vpc.create_tags(Tags=[{"Key": "Name", "Value": "myvpc"}])
public_subnet.create_tags(Tags=[{"Key": "Name", "Value": "myvpc_public_subnet"}])
private_subnet.create_tags(Tags=[{"Key": "Name", "Value": "myvpc_private_subnet"}])
internet_gateway.create_tags(Tags=[{"Key": "Name", "Value": "myvpc_internet_gateway"}])
public_route_table.create_tags(Tags=[{"Key": "Name", "Value": "myvpc_public_route_table"}])
private_route_table.create_tags(Tags=[{"Key": "Name", "Value": "myvpc_private_route_table"}])
security_group.create_tags(Tags=[{"Key": "Name", "Value": "myvpc_security_group"}])
create_tag = ec2_client.create_tags(Resources=[ec2_instance_id], Tags=[{'Key': 'Name','Value': 'myvpc_ec2_instance'}])

# print webserver and dns name
ec2_instance = ec2_client.describe_instances(Filters=[{'Name': 'tag:Name','Values': ['myvpc_ec2_instance']},{'Name': 'instance-state-name','Values': ['running']}])
ec2_public_dns_name = ec2_instance["Reservations"][0]["Instances"][0]["PublicDnsName"]
print('Webserver URL: ' + ec2_public_dns_name)

#### Create a volume ####
# create_volume(size, zone, snapshot=None, volume_type=None, iops=None)
conn = boto.ec2.connect_to_region("us-east-2")
vol = conn.create_volume(10, "us-east-2a")
print ('Volume Id: ', vol.id)

# Add a Name tag to the new volume so we can find it.
conn.create_tags([vol.id], {"Name":"ali-volume"})

# We can check if the volume is now ready and available:
curr_vol = conn.get_all_volumes([vol.id])[0]
while curr_vol.status == 'creating':
    curr_vol = conn.get_all_volumes([vol.id])[0]
    print ('Current Volume Status: ', curr_vol.status)
    time.sleep(2)
print ('Current Volume Zone: ', curr_vol.zone)

#### Attach a volume ####
result = conn.attach_volume (vol.id, ec2_instance_id, "/dev/sdf")
print ('Attach Volume Result: ', result)