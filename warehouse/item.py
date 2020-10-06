class Item:
    id = 0
    title = ""
    category = ""
    stock = 0
    price = 0.0

    def __init__(self, id, title, category, stock, price):
      self.id = id
      self.title = title
      self.category = category
      self.stock = stock
      self.price = price


    def to_string():
        print("{")
        print(" id: " + str(id))
        print(" title: " + title)
        print(" category: " + category)
        print(" stock: " + str(stock))
        print(" price: " + str(price))
        print("}")