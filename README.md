# Mpesa Integrated ecommerce website.
This is an e-commerce system that has an HTML, CSS, JavaScript, and SCSS frontend, and a Django backend. The ecommerce system is integrated with Mpesa, allowing users to purchase products. When a user makes a purchase, an Mpesa prompt message is sent to their phone, asking them to enter their Mpesa PIN. Additionally, the ecommerce system includes authentication features, enabling users to sign up, log in, and log outi. Below are screenshots demonstrating the process of a user purchasing a product.
![page1](https://github.com/Kimani-dev931/Django-Ecommerce/assets/77829096/925a0c01-9419-491f-accf-366893217042)
![page2](https://github.com/Kimani-dev931/Django-Ecommerce/assets/77829096/6512cbf1-a96b-4a52-92c5-b79ec17135fe)
![page3](https://github.com/Kimani-dev931/Django-Ecommerce/assets/77829096/de964dae-edc1-4bd8-aab3-bdf7e144e569)
![page4](https://github.com/Kimani-dev931/Django-Ecommerce/assets/77829096/1fb0c5c0-2ed0-4c17-97cd-484ce37c3338)
![page5](https://github.com/Kimani-dev931/Django-Ecommerce/assets/77829096/b774d6dd-d39f-4258-8a5d-414fe1746ef5)
![page6](https://github.com/Kimani-dev931/Django-Ecommerce/assets/77829096/521cf488-dcc2-4523-a2f7-5ef555b3b479)
![Products upload Admin section](https://github.com/Kimani-dev931/Mpesa-Integrated-Django-Ecommerce-Website/assets/77829096/b8b17e3f-4cc1-4715-a871-126d8f49776e)

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
