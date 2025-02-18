FROM node:23-alpine3.20

RUN mkdir /server
COPY . /server
RUN rm -rf /server/node_modules
WORKDIR /server
RUN npm install -g pnpm
RUN pnpm install

CMD ["pnpm", "dev"]