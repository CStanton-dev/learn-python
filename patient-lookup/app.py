# importing date class from datetime module
from datetime import date

# creating the date object of today's date
todays_date = date.today()

# user input
name = input('Input patient name: ')
birth_year = input('Input patient birth year: ')

# calculating patient age
patient_age = todays_date.year - int(birth_year)

# retrevial of patient information
print('Retrieving patient information for: ' + name)