#!/bin/bash -ex

# Update yum
yum -y update

#Install nodejs
yum -y install nodejs

# Create a dedicated directory for the application
mkdir -p /var/app

# Get the app from S3
wget https://aws-tc-largeobjects.s3-us-west-2.amazonaws.com/ILT-TF-100-TECESS-5/app/app.zip

# Extract it to the desired folder
unzip app.zip -d /var/app/
cd /var/app/

# Install dependencies
npm install

# Start the app
npm start
