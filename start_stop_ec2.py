import boto3
import sys

ec2 = boto3.client('ec2')

filters = [{'Name': 'tag:env', 'Values': [sys.argv[1]]},
 {'Name': 'tag:Name', 'Values': [sys.argv[2]]},
 {'Name': 'tag:Owner', 'Values': [sys.argv[3]]},
 {'Name': 'tag:Project', 'Values': [sys.argv[4]]},
 {'Name': 'tag:Purpose', 'Values': [sys.argv[5]]}

 ]

response = ec2.describe_instances(Filters=filters)

instanceIds = []

for r in response['Reservations']:
 for i in r['Instances']:
 instanceIds.append(i['InstanceId'])

print(instanceIds)

if sys.argv[6] == "Stop":
 response = ec2.stop_instances(
 InstanceIds=instanceIds,

 )

else:
 response = ec2.start_instances(
 InstanceIds=instanceIds
 )

print(response)
