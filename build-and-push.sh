sudo docker build -t $1 .
aws ecr get-login-password --region us-east-1 | sudo docker login --username AWS --password-stdin 133420669210.dkr.ecr.us-east-1.amazonaws.com
sudo docker tag $1:latest 133420669210.dkr.ecr.us-east-1.amazonaws.com/$1:latest
sudo docker push 133420669210.dkr.ecr.us-east-1.amazonaws.com/$1:latest