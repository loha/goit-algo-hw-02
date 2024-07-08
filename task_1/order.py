class Order:
  def __init__(
      self,
      id: str,
      name: str,
      surname: str,
      details: str,
      price: float,
  ):
    self.id = id
    self.name = name
    self.surname = surname
    self.details = details
    self.price = price
  
  def __str__(self) -> str:
    return f"Id: {self.id}. Name: {self.name} {self.surname}. Details: {self.details}. Price: {self.price}"