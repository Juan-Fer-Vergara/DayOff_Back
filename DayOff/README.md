# DayOff Backend

Backend desarrollado en Django + Django REST Framework para DayOff.

## ¿Cómo ejecutar el proyecto?

```bash
git clone https://github.com/<usuario>/DayOff_Back.git
cd DayOff_Back

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
