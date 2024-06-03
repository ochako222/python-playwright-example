headless:
	pytest -s
ui.qa:
	ENV=qa pytest --headed -s
ui.beta:
	ENV=beta pytest --headed -s 
single:
	pytest test_login.py