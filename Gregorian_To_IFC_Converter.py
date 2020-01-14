months = ["January", "February", "March", "April", "May", "June", "Sol", "July", "August", "September", "October", "November", "December"]
current_days = [31,28,31,30,31,30,31,31,30,31,30,31]
current_leap_days = [31,29,31,30,31,30,31,31,30,31,30,31]
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def date_calculator():
  while (True):
    print("Please enter the date you want to convert in the format MM/DD/YYYY. Type 'END' to exit.")
    date = input("> ").split("/")
    if (date[0] == "END"):
      break
    elif ((int(date[0]) > 12) or (int(date[0]) < 1) or (int(date[1]) < 1)):
      print("Invalid Input")
    else:
      month = int(date[0])
      day = int(date[1])
      year = int(date[2])
      leap = False
      if (year % 4 == 0):
        if ((year % 400 == 0) or (year % 100 != 0)):
          leap = True
      if (current_days[month - 1] < day):
        if ((month != 2) or (day != 29) or not leap):
          print("Invalid Input")
        else:
          calc_date(day, month, year, leap)
      else:
        calc_date(day, month, year, leap)

def calc_date(day, month, year, leap):
  num_days = day
  for x in range(month - 1):
    if (leap):
      num_days += current_leap_days[x]
    else:
      num_days += current_days[x]
  if ((not leap and num_days == 365) or (leap and num_days == 366)):
    print("That's Year Day!")
  elif ((not leap and num_days == 364) or (leap and num_days == 365)):
    print("That is Saturday 28 December.")
  elif (leap and num_days == 169):
    print("That's Leap Day!")
  else:
    if (leap and num_days > 169):
      num_days -= 1
    new_day = days[int((num_days % 28) % 7) - 1]
    if ((num_days % 28) == 0):
      new_month = months[(int(num_days / 28) - 1)]
      num_days = 28
    else:
      new_month = months[int(num_days / 28)]
      num_days = num_days % 28
    print("That is "+ new_day +" "+ str(num_days) +" "+ new_month +".")     
        
date_calculator()
