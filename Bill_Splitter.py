#Keaton Smith 1/21/2020

#Function that calculates each patron's share of the bill and displays it to the user
def Calc_Total_and_Tip(patrons, subbills):
  #Prompt for the tax
  print("What was the tax?")
  tax = float(input("> "))
  #Prompt for the tip
  print("What was the tip?")
  tip = float(input("> "))
  #Determine subtotal before tax and tip
  subtotal = sum(subbills)
  iter = 0
  #Do the calculation and display results
  for person in patrons:
    subbill = subbills[iter]
    #The patron's percentage of the subtotal which determines percentage of tax and tip
    percentage = subbill / subtotal
    print(person)
    amount = (subbill + (percentage * tax) + (percentage * tip))
    print(round(amount, 2))
    print("==============")
    #Move to next patron on the list
    iter += 1
          
#Takes in all the items on the bill preceded by their owner and then calls the calculating function
def Items_On_Bill(patrons):
  #Prompt for input
  print("Please enter the number of the person followed by the amount for each item.")
  print("When you are finished type 'END'.")
  #Create and fill the list that will hold each patron's subtotal
  subbills = []
  for x in patrons:
    subbills.append(0.0)
  #Display the list of patrons for ease of use
  print(patrons)
  #Take in input for which patron (they're position in the list above) followed by the amount
  while (True):
    patron = input("> ")
    #Allow user to state when finished
    if (patron == "END"):
      break
    subbills[int(patron)] += float(input("> "))
  #Calls the calculation function
  Calc_Total_and_Tip(patrons, subbills)

#Get the list of the people that have items on the bill
def People_On_Bill():
  #Instantiate variables for use later
  patrons = []
  names = ""
  #Prompt the user for input
  print("Hello, please enter the names of the people on the bill one at a time.")
  print("When you are finished type 'END'.")
  while (True):
    names = input("> ")
    #Allow the user to state when they are finished
    if (names == "END"):
      break
    patrons.append(names)
  #Call the function that handles assigning bill items to a customer
  Items_On_Bill(patrons)

#Call the first function to kick off the program
People_On_Bill()
