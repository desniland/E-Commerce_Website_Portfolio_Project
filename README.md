# Mpesa Integrated ecommerce website.
This is an e-commerce system that has an HTML, CSS, JavaScript, and SCSS frontend, and a Django backend. The ecommerce system is integrated with Mpesa, allowing users to purchase products. When a user makes a purchase, an Mpesa prompt message is sent to their phone, asking them to enter their Mpesa PIN. Additionally, the ecommerce system includes authentication features, enabling users to sign up, log in, and log outi. Below are screenshots demonstrating the process of a user purchasing a product.

Installation
git clone https://github.com/desniland/E-Commerce_Website_Portfolio_Project.git

cd E-Commerce_Website_Portfolio_Project

pip install virtualenv

virtualenv env

For Mac/ Linux
source env/bin/activate

For Window
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
Password: ''

Demo: http://127.0.0.1:8000/
