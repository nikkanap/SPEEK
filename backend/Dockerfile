FROM python:3.12

# Copy the files in the main dir to /app
WORKDIR /app 
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000 