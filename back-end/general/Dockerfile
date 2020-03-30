FROM node:12.10.0-alpine

WORKDIR /app
ADD ./package* ./
RUN npm install
COPY ./src/ ./src

RUN mkdir -p /warehouse
EXPOSE 3000

CMD npm run start
