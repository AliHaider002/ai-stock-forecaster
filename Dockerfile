# Use Node.js base image
FROM node:alpine3.18

# Install Python and pip
RUN apk add --no-cache python3 py3-pip

# Set the working directory
WORKDIR /app

# Copy package.json and install Node.js dependencies
COPY package.json ./
RUN npm install -f

# Copy Python requirements and install them
COPY requirements.txt ./
RUN pip3 install -r requirements.txt

# Copy the rest of your application code
COPY . .

# Expose the application port
EXPOSE 8086

# Start the Node.js application
CMD [ "npm", "run", "dev" ]
