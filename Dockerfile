FROM public.ecr.aws/lambda/python:3.9

# Copy function code
COPY app.py ${LAMBDA_TASK_ROOT}

# Install libs

# Install wget, tar, libsndfile and sox
RUN yum install wget tar xz libsndfile sox -y

# Install FFmpeg
RUN mkdir /usr/local/bin/ffmpeg
RUN wget -O /tmp/ffmpeg.tar.xz https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz
RUN tar xvf /tmp/ffmpeg.tar.xz -C /usr/local/bin/ffmpeg
RUN ln -s /usr/local/bin/ffmpeg/ffmpeg /usr/bin/ffmpeg

# Install the function's dependencies using file requirements.txt
# from your project folder.

COPY requirements.txt  .
RUN pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}" --no-cache-dir # --no-cache-dir might be useful

# Do some extra stuff
RUN mkdir /tmp/smg-serverless
COPY music_genre_classification/ /tmp/smg-serverless

COPY music_genre_classification .

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "app.handler" ]