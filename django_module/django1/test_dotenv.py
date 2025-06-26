import os
from dotenv import load_dotenv

# load_dotenv('/home/qospanulan/edu/justcode/python25/django_module/django1/.env')


# print(type(os.environ))
password = os.environ.get('DB_PASSWORD', 'password')

print(password)

