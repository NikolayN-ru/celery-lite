source venv/bin/activate
#
pip install requarements.txt
#
celery -A app worker -l INFO
#
./manage.py runserver
