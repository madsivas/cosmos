set COSMOS_CONFIG_DIR=C:\dev\ws\cosmos\config
set COSMOS_ENV=development

set COSMOS_OVERRIDE_CFG=override
rem python ./manage.py $*

echo "Running server"
python ./manage.py runserver_debug