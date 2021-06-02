# pull the base image
FROM node:alpine

# set the working direction
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install app dependencies
COPY package.json ./

COPY package-lock.json ./

RUN npm install
RUN npm install -g serve

# add app
COPY . ./
RUN npm run build

# start app
# deployment recipe from https://create-react-app.dev/docs/deployment/#static-server
CMD ["serve", "-s", "build", "-l", "3000"]
