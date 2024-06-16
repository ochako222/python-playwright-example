headless:
	pytest -s
ui.qa:
	ENV=qa pytest --headed -s
ui.qa.debug:
	ENV=qa PWDEBUG=1 pytest --headed -s
ui.beta:
	ENV=beta pytest --headed -s 
single:
	pytest test_login.py