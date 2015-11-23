# agile-fusion-test-task
AgileFusion test task

### Init

    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt
    configure settings_local.py (DATABASES - PostgresSQL and DEBUG = True)
    python manage.py migrate


### After project init to run:

    python manage.py runserver --verbosity 3
    celery -A taxi worker -B -l info
    python test_load_divers.py
    python test_load_clients.py
