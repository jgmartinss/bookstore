clean:
	rm -rf db.sqlite3
help:
	@echo '--------------------Bookstore-------------------------'
	@echo '                                                      '
	@echo 'Usage:                                                '
	@echo '------> run         Run project                       '
	@echo '------> shell       Shell command line                '
	@echo '------> test        Run tests                         '
	@echo '------> test        BDD Run tests                     '
	@echo '------> createuser  Create superuser                  '
	@echo '------> migrations  Run makemigrations                '
	@echo '------> migrate     Run migrate                       '
	@echo '------> setup       Setup the project                 '
run:
	python3 manage.py runserver
createuser:
	python3 manage.py createsuperuser --email='admin@email.com' 
migrations:
	python3 manage.py makemigrations
migrate:
	python3 manage.py migrate
shell:
	python3 manage.py shell
test:
	python3 manage.py test -n
test_bdd:
	python3 manage.py test tests/bdd
setup:
	pipenv install
	pipenv install -d 
	python contrib/env_gen.py
	python3 manage.py makemigrations
	python3 manage.py migrate
diagram:
	python manage.py graph_models -a -o diagram.png
populate_accounts:
	python manage.py generate_users 20
populate_customers:
	python manage.py generate_address 20
	python manage.py generate_reviews 30
populate_coupons:
	python manage.py generate_coupons 15
populate_newslatter:
	python manage.py generate_subscribes 15
populate_catalog:
	python manage.py generate_authors 20
	python manage.py generate_categories 10
	python manage.py generate_publishers 10
	python manage.py generate_books 30
populate_db: populate_accounts populate_coupons populate_newslatter populate_catalog populate_customers



