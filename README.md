# Simple_solution_test_task
Тестовое задание для компании "Простые решения"

## Description
	Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:
· 	Django Модель Item с полями (name, description, price)
· 	API с двумя методами:
· 	GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса
· 	GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на /buy/{id}, получение session_id и далее с помощью JS библиотеки Stripe происходить редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id)
· 	Запуск используя Docker
· 	Использование environment variables
· 	Просмотр Django Моделей в Django Admin панели
· 	Запуск приложения на удаленном сервере, доступном для тестирования
· 	Модель Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order c общей стоимостью всех Items
· 	Модели Discount, Tax, которые можно прикрепить к модели Order и связать с соответствующими атрибутами при создании платежа в Stripe - в таком случае они корректно отображаются в Stripe Checkout форме.
· 	Добавить поле Item.currency, создать 2 Stripe Keypair на две разные валюты и в зависимости от валюты выбранного товара предлагать оплату в соответствующей валюте
· 	Реализовать не Stripe Session, а Stripe Payment Intent.

## Technologies

- Python 3.10
- Django 4.2.4
- stripe-7.9.0
- Docker

## Launching the Project in Development Mode

- Set up and activate the virtual environment.
- Install dependencies from the requirements.txt file:

```
pip install -r requirements.txt
```

In the folder containing manage.py, run the command:
```
python3 manage.py runserver
```
