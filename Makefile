serve:
	python3 manage.py runserver 8100

migrations:
	python3 manage.py makemigrations
	python3 manage.py migrate