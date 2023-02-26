FROM node:lts-slim as base
WORKDIR /app

COPY package.json yarn.lock ./
RUN yarn install --pure-lockfile

ENV PATH /app/node_modules/.bin:$PATH

COPY . .

FROM base as dev

EXPOSE 5173

FROM base as builder

RUN yarn build

FROM nginx:latest as prod
WORKDIR /
RUN rm -rf /etc/nginx/conf.d
COPY conf /etc/nginx

COPY --from=builder /app/dist ./dist

EXPOSE 80

CMD ["/bin/bash", "-c", "nginx -g \"daemon off;\""]
