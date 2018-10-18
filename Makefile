clean:
	rm -rf bookstore/db.sqlite3
run:
	python3 manage.py runserver
migrate:
	python3 manage.py migrate
migrations:
	python3 manage.py makemigrations
createuser:
	python3 manage.py createsuperuser
shell:
	python3 manage.py shell
test:
	python3 manage.py test
install:
	pip3 install -r requirements.txt
depends:
	pip3 freeze > requirements.txt
rebuild: clean migrations migrate

test_bdd:
	python3 manage.py test tests/bdd
