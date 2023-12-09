#!/bin/sh

trap "trap - SIGTERM && kill -- -$$" SIGINT SIGTERM EXIT

# config
export FLASK_DEBUG=1
export RECALL_PORT=5001
export RANK_PORT=5002
export API_PORT=5003
export DATASET_PATH='/Users/marioxzhang/Desktop/recommendation system/dataset'

export RANK_ENDPOINT="http://localhost:${RANK_PORT}"
export RECALL_ENDPOINT="http://localhost:${RECALL_PORT}"

# recall service
cd recall-service && source venv/bin/activate && ./start.sh &
echo ">> Recall Service started"
sleep 3

# rank service
cd rank-service && source venv/bin/activate && ./start.sh &
echo ">> Rank Service started"
sleep 3

# api service
cd api-service && source venv/bin/activate && ./start.sh &
echo ">> API Service started"
sleep 3

# web service
cd web-service && ./start.sh &
echo ">> Web Service started"

sleep 9999999
