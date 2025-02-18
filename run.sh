#!/bin/bash
TOP_LEVEL=$(pwd)

cd $TOP_LEVEL
cd ./packages/server && docker build . -t newsly-server:latest
cd $TOP_LEVEL
cd ./packages/web && docker build . -t newsly-web:latest

docker compose up -d