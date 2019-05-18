install_app:
	pip install -e .

init_db: install_app
	python zeus/scripts/create_db.py

seed_spots: install_app
	python zeus/scripts/seed_spots.py

run_app: install_app
	(export FLASK_APP=./zeus && export FLASK_ENV=development && flask run)
