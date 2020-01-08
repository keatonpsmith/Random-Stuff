def Calc_Total_and_Tip(patrons, subbills):
  print("What was the tax?")
  tax = float(input("> "))
  print("What was the tip?")
  tip = float(input("> "))
  subtotal = sum(subbills)
  iter = 0
  for person in patrons:
    subbill = subbills[iter]
    percentage = subbill / subtotal
    print(person)
    print(subbill + (percentage * tax) + (percentage * tip))
    print("==============")
    iter += 1

def Items_On_Bill(patrons):
  print("Please enter the number of the person followed by the amount for each item.")
  print("When you are finished type 'END'.")
  subbills = []
  for x in patrons:
    subbills.append(0.0)
  print(patrons)
  while (True):
    patron = input("> ")
    if (patron == "END"):
      break
    subbills[int(patron)] += float(input("> "))
  Calc_Total_and_Tip(patrons, subbills)

def People_On_Bill():
  names = ""
  print("Hello, please enter the names of the people on the bill one at a time.")
  print("When you are finished type 'END'.")
  patrons = []
  while (True):
    names = input("> ")
    if (names == "END"):
      break
    patrons.append(names)
  Items_On_Bill(patrons)

People_On_Bill()