FROM node:12.10.0-alpine

WORKDIR /app
ADD ./package* ./
RUN npm install
COPY ./src/ ./src

EXPOSE 3000

CMD npm run start
