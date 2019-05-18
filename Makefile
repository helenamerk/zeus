init_db:
	python db/models.py

run_app:
	FLASK_APP=./zeus FLASK_ENV=development flask run
