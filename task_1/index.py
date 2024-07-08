import sys
from queue import Queue
from order import Order
from randomize import generate_random_name, generate_id, generate_price, generate_random_string

queue = Queue()

def generate_request():
  id = generate_id()
  name, surname = generate_random_name()
  price = generate_price()
  details = generate_random_string(20)

  order = Order(
    id = id,
    name = name,
    surname = surname,
    details = details,
    price = price
  )

  queue.put(order)

def process_request():
  not_empty_queue = queue.qsize() > 0 

  if not_empty_queue:
    order = queue.get()
    str_order = str(order)
    print(f'Order {str_order} processed')
  else:
    print('No orders to process')

def main():
  while True:
    command_value = str(input("Enter the command('y' or 'n'): \n~$/"))

    if command_value == 'y':
      generate_request()
      process_request()
    else:
      sys.exit(0)

main()
