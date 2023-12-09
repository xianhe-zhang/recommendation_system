#!/bin/sh

if [ -z "${DATASET_PATH}" ]; then
    export DATASET_PATH='../../data/anime'
fi

export FLASK_APP=app
export FLASK_RUN_PORT=5001


flask run
