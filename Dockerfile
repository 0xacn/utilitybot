# Pull python3.6 image from docker
FROM python:3.6

# Make sure we are in the bot directory where code is stored
WORKDIR /bot
 
# Copy the depedencies from the file
COPY requirements.txt .
# Install them with pip
RUN pip install -r requirements.txt

COPY /utilitybot . 

# Run the main file in the container
CMD ["python", "utilitybot.py"]