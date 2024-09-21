FROM node:16

WORKDIR /app

# Copy package files and install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the source code
COPY . /app/

# Expose the development server port
EXPOSE 3000

# Use npm start to run the React app in development mode
CMD ["npm", "start"]
