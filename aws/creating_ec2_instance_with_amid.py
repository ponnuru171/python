import boto3

ec2 = boto3.resource('ec2')

# create a new EC2 instance

New_instances = ec2.create_instances(

     ImageId='ami-00b6a8a2bd28daf19',           #mention the required ami id

     MinCount=1,

     MaxCount=2,

     InstanceType = 't2.micro',

     KeyName='ec2-keypair')                     #mention the key pair


print("ec2 insytance created")
