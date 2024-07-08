import random
import string
from uuid import uuid4

def generate_random_name() -> tuple:
  first_names = ['Ivan', 'Olena', 'Andriy', 'Nadiya', 'Viktor', 'Kateryna']
  last_names = ['Shevchenko', 'Kovalenko', 'Petryk', 'Ivanenko', 'Tkachenko', 'Sydorenko']
  
  first_name = random.choice(first_names)
  last_name = random.choice(last_names)
  
  return  first_name, last_name

def generate_id() -> str:
  return str(uuid4())

def generate_price() -> float:
  return random.uniform(0, 10)

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for i in range(length))
    return random_string