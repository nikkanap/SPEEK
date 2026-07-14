FROM python:3.12

# Copy the files in the main dir to /app
WORKDIR /app 
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .
EXPOSE 8000 