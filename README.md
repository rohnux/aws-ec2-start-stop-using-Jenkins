# aws-ec2-start-stop Using Jenkins Job
Python script to start and stop aws-ecs instance using Jenkins.


## Requirements

### Python Modules in Jenkin Server

If you never used [Amazon Web Services](https://aws.amazon.com/) with Python before, you have to install two additional modules:

    pip install python3.5
    pip install boto3

### AWS CLI in Jenkin Server
After you've installed the AWS CLI. Then run the following command:

        aws configure

    Enter

    * your AWS Access Key ID and
    * your AWS Secret Access Key.
    * As default region name enter your Availability Zone (AZ) and
    * use "json" as default output format.    


###Create the Parametized Job
All the arguments are taken from parameters. The code is made generic. Any aws-ec2 instance can be start or stop based on Tags and AWS_PROFILE you choose from the parameter.    


###Write this in the Execute shell in Jenkins Job
export AWS_PROFILE= $Profile
python3.5 start_stop_ec2.py  $env $Name $Owner $Project $Purpose $State
