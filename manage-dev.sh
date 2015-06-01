#!/bin/sh

set -e
export COSMOS_CONFIG_DIR="$(pwd)/config"
export COSMOS_ENV="development"

export COSMOS_OVERRIDE_CFG="override"
python ./manage.py $*
