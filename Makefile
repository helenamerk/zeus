# Create database tables
init_db: venv
	. venv/bin/activate; python db/models.py
