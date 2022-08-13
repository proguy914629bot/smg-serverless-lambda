# Spotify Music Genre on AWS Lambda

## Setup:
The below setup is listed for Local and AWS Lambda setup.

It is recommended to run the AWS Lambda setup before running the Local setup.

### AWS Lambda Setup:
1. Make sure you are using an AWS Linux Operating System and you have installed docker. The free tier of EC2 Instance with AWS Linux should be enough to run this.

2. Clone the repository:
```bash
$ git clone --single-branch --branch aws-lambda https://github.com/proguy914629bot/smg-serverless-lambda
```

3. Make sure you have installed AWS CLI and configured it with your credentials using `aws configure`.

3. Build docker image (use sudo/root if needed)
```bash
$ docker build -t smg-serverless-lambda .
```

4. Create an ECR repository named `smg-serverless-lambda`

4. Login to AWS ECR (use sudo/root if needed). Replace `<account-id>` to your AWS account id.
```bash
$ aws ecr get-login-password | sudo docker login --username AWS --password-stdin <account-id>.dkr.ecr.us-east-1.amazonaws.com
```

5. Tag the image (use sudo/root if needed). Replace `<account-id>` to your AWS account id.
```bash
sudo docker tag smg-serverless-lambda:latest <account-id>.dkr.ecr.us-east-1.amazonaws.com/smg-serverless-lambda:latest
```

6. Push docker image to ECR (use sudo/root if needed). Replace `<account-id>` to your AWS account id.
```bash
$ sudo docker push <account-id>.dkr.ecr.us-east-1.amazonaws.com/smg-serverless-lambda:latest
```

7. Create an AWS Lambda function named `smg-serverless-lambda` with the docker image linked to it.

8. Add a trigger (specifically an API Gateway trigger) as a `Rest API` with the Security as `Open`.

9. Continue with the [Local Setup](#local-setup).

### Local Setup:
1. Clone the repository:
```bash 
$ git clone --single-branch --branch local https://github.com/proguy914629bot/smg-serverless-lambda
```

2. Install [FFMpeg](https://ffmpeg.org/download.html) and [SoX](http://sox.sourceforge.net/) and add it to your PATH (if necessary).

3. Install dependencies:
```bash
$ cd smg-serverless-lambda
$ pip install --upgrade -r requirements.txt
```

4. Edit the `config.json` file. The following things that are required to be edited are:
- `API_URL`: The URL of your AWS Lambda API Gateway.

5. Continue with [Running](#running).

### Running:
All steps are going to be ran on local and in the same directory as the `config.json` file.

1. Run the script:
```bash
$ python3 main.py
```

2. Follow the steps printed/displayed in your terminal/console.

3. Done!