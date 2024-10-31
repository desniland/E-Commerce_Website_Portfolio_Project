# Mpesa Integrated ecommerce website.
This is an e-commerce system that has an HTML, CSS, JavaScript, and SCSS frontend, and a Django backend. The ecommerce system is integrated with Paypal, allowing users to purchase products. When a user makes a purchase, a Paypal prompt message is sent to their phone, asking them to enter their Credit Card Information. Additionally, the ecommerce system includes authentication features, enabling users to sign up, log in, and log out. Below are screenshots demonstrating the process of a user purchasing a product.

![home-pic1](https://github.com/user-attachments/assets/262a07a2-8763-433f-b051-78f0e39e669c)
![Items-pic2](https://github.com/user-attachments/assets/66a4fe31-cc69-4928-b56c-1dba4f958bd3)
![cart-pic3](https://github.com/user-attachments/assets/27584851-e9b5-43bd-bfc6-f356743c4028)
![pic4](https://github.com/user-attachments/assets/a8617eb4-927d-40b6-8d23-dd4bcfdbd696)
![checkout-pic5](https://github.com/user-attachments/assets/13b349c9-825a-490c-a421-042b11c48725)
![pay-pic6](https://github.com/user-attachments/assets/554a28ba-4e65-4075-8d10-61d6569eba4f)

Installation
git clone https://github.com/desniland/E-Commerce_Website_Portfolio_Project.git


cd E-Commerce_Website_Portfolio_Project


pip install virtualenv


virtualenv env

For Mac/ Linux:

source env/bin/activate

For Window:

env\Scripts\activate

pip install -r requirements.txt


Install below version in terminal and 'New Version will face version conflict error'

pip install Django==2.2.4

python -m pip install django-allauth==0.40.0

pip install django-crispy-forms==1.7.2

pip install Pillow

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

For Admin Login

python manage.py createsuperuser

Username : admin

Password: '12345678'

Demo: http://127.0.0.1:8000/ or 3000
 
