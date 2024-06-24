reporter = --html-report=./report/report.html
headless:
	pytest -s $(reporter)
single:
	pytest tests/test_login.py -s $(reporter)
ui.qa:
	ENV=qa pytest --headed -s
ui.qa.debug:
	ENV=qa PWDEBUG=1 pytest --headed -s
ui.beta:
	ENV=beta pytest --headed -s
