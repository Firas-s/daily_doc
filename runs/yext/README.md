## Build
    docker build --tag eu.gcr.io/flows-yext-dev/yext .

## Run Locally
    docker run --rm -p 9090:8080 -e PORT=8080 eu.gcr.io/flows-yext-dev/yext

## Run in development mode
    docker run --rm -p 9090:8080 -e PORT=8080 -e ENV=dev -v <key file>:/root/key.json -e GOOGLE_APPLICATION_CREDENTIALS=/root/key.json -v <src folder>:/app/src eu.gcr.io/flows-yext-dev/yext

## Call the API

    curl -d '{"message":{"data": "TEST"}}' -H "Content-Type: application/json" -X POST http://localhost:9090


docker run --rm -p 9090:8080 -e PORT=8080 -e ENV=dev -v /home/rahma/projects/flows/yext/runs/yext/src:/app/src eu.gcr.io/flows-yext-dev/yext



curl -X POST http://localhost:9090
