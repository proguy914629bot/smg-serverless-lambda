FROM public.ecr.aws/lambda/python:3.9

# Copy function code
COPY app.py ${LAMBDA_TASK_ROOT}

# Install libs
RUN yum install ffmpeg -y
RUN yum install gstreamer1.0-plugins-base gstreamer1.0-plugins-ugly -y
RUN yum install libsndfile -y

# Install the function's dependencies using file requirements.txt
# from your project folder.

COPY requirements.txt  .
RUN pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Do some extra stuff
RUN mkdir /tmp/smg-serverless
COPY music_genre_classification/ /tmp/smg-serverless

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "app.handler" ]