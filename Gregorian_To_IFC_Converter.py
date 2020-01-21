#Keaton Smith 1/21/2020

#Setting up lists for use later, each contains all the possible lengths or names of months and the days of the week:
months = ["January", "February", "March", "April", "May", "June", "Sol", "July", "August", "September", "October", "November", "December"]
current_days = [31,28,31,30,31,30,31,31,30,31,30,31]
current_leap_days = [31,29,31,30,31,30,31,31,30,31,30,31]
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

#Function to take in user input and do some pre-processing:
def date_calculator():
  while (True):
    #Get input
    print("Please enter the date you want to convert in the format MM/DD/YYYY. Type 'END' to exit.")
    date = input("> ").split("/")
    #Escape case for when user is done
    if (date[0] == "END"):
      break
    #Invalid input checks
    elif ((int(date[0]) > 12) or (int(date[0]) < 1) or (int(date[1]) < 1)):
      print("Invalid Input")
    #Pre-processing and calling actual date calculation
    else:
      #Seperating out various elements of input
      month = int(date[0])
      day = int(date[1])
      year = int(date[2])
      leap = False
      #Determine if it is a leap year
      if (year % 4 == 0):
        if ((year % 400 == 0) or (year % 100 != 0)):
          leap = True
      #Further invalid input checks, for example asking for the conversion of August 59th
      if (current_days[month - 1] < day):
        if ((month != 2) or (day != 29) or not leap):
          print("Invalid Input")
        else:
          #Calling the calculation function
          calc_date(day, month, year, leap)
      else:
        calc_date(day, month, year, leap)

#Calculates the new date and presents it to the user
def calc_date(day, month, year, leap):
  #Calculating how many days have passed since January 1st
  num_days = day
  for x in range(month - 1):
    if (leap):
      num_days += current_leap_days[x]
    else:
      num_days += current_days[x]
  #Special cases
  if ((not leap and num_days == 365) or (leap and num_days == 366)):
    print("That's Year Day!")
  elif ((not leap and num_days == 364) or (leap and num_days == 365)):
    print("That is Saturday 28 December.")
  elif (leap and num_days == 169):
    print("That's Leap Day!")
  #Calculations for if it isn't a special case
  else:
    #Accounting for the offset of between leap years in the two calendars
    if (leap and num_days > 169):
      num_days -= 1
    #Determine which day of the week it falls on
    new_day = days[int((num_days % 28) % 7) - 1]
    #Figure out the new Month, the first case is only for if the date entered would be on the last day of a month.
    if ((num_days % 28) == 0):
      new_month = months[(int(num_days / 28) - 1)]
      num_days = 28
    else:
      new_month = months[int(num_days / 28)]
      num_days = num_days % 28
    #Display new date to user
    print("That is "+ new_day +" "+ str(num_days) +" "+ new_month +".")     

#Call the first function to kick off the program
date_calculator()
