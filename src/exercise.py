from product import Product
def main():
    #write your code below this line
  tape_measure = Product("Tape measure")
  plaster = Product.with_location("Plaster", "home improvement section")
  tyre = Product.with_weight("Tyre", 5)

  print(tape_measure)
  print(plaster)
  print(tyre)
  pass
if __name__ == '__main__':
    main()
