import datetime
import time
ct=datetime.datetime.now()
print(ct)
time.sleep(10)
ct1=datetime.datetime.now()
print(ct1)
print(ct1-ct)