from datetime import date

# assigning today's date to today's variable
today = date.today()
formatted_date = today.strftime("%Y-%m-%d")

## Function definition
# Extracting day and month and year from today's date
def readDate(formatted_date) :
	month = int(formatted_date[5:7])
	day = int(formatted_date[8:])
	year = int(formatted_date[0:4])
	return (month, day, year) # Returns a tuple.
# Computing the number of days till New Year
def Countdown(day,month) :
	if month == 12:
	    print (f"Days until New Year's Day: {(31-day+1)}") 

# Function call: use tuple assignment:
(month, day, year) = readDate(formatted_date)
Countdown(day,month)