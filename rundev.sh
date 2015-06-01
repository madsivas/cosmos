#!/bin/sh

set -e
export COSMOS_CONFIG_DIR="$(pwd)/config"
export COSMOS_ENV="development"
export COSMOS_OVERRIDE_CFG="override"

echo "Compiling translations..."
cd locale
./recompile.sh
cd ..


echo "Running server"
python ./manage.py runserver_debug
