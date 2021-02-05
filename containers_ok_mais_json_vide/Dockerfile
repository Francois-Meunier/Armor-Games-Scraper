#Import python 3.8
FROM python:3.8-buster

#Define the directory of the application
WORKDIR /app

# Copy the file to the Docker image
COPY requirements.txt .

# Run the command to install python packages
RUN pip install -r requirements.txt

# Copy the application repository in the Docker image
COPY /app .

# Run the command to get the games info
RUN python scrap_infos.py
# python app.py

# The command to launch the app
CMD ["python", "app.py"]