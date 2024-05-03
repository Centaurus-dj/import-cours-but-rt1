#!/bin/sh

docker compose rm -s -f
docker compose create --build --force-recreate
docker compose start
docker compose ps -a