headless:
	pytest -s
ui:
	pytest --headed
single:
	pytest test_login.py