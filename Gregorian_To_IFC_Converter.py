def date_calculator():
  while (True):
    months = ["January", "February", "March", "April", "May", "June", "Sol", "July", "August", "September", "October", "November", "December"]
    current_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    print("Please enter the date you want to convert in the format MM/DD. Type 'END' to exit.")
    date = input("> ").split("/")
    if (date[0] == "END"):
      break
    month = int(date[0])
    day = int(date[1])
    num_days = day
    for x in range(month - 1):
      num_days += current_days[x]
    if (num_days == 365):
      print("That's Year Day!")
    elif (num_days == 364):
      print("That is Saturday 28 December.")
    else:
      new_month = months[int(num_days / 28)]
      new_day = days[int((num_days % 28) % 7) - 1]
      if ((num_days % 28) == 0):
        num_days = 28
      else:
        num_days = num_days % 28
      print("That is "+ new_day +" "+ str(num_days) +" "+ new_month +".")

date_calculator()