# pull official base image
FROM python:3.8.2-alpine

# set work directory
RUN mkdir -p /app
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev



# install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip install -r requirements.txt



#copy project
COPY . .

# copy entrypoint.sh
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

# run entrypoint.sh
# ENTRYPOINkT ["entrypoint.sh"]