# Python script to populate country geographical information
# From initial country name entered by user
# Using countryinfo module

# First instaled counrtyinfo module in this "ML-using-python" virstual environment
# using pip > python3 -m pip install countryinfo

import countryinfo

from countryinfo import CountryInfo

# user input for Country Name
count_user_defined = input("Enter country name here:")

# retrive details (info) from country imputted by user

country = CountryInfo(count_user_defined)

# Using different country. functions to retrieve 
# different type of country information

print("Capital is: ",country.capital())
print("Currency is: ",country.currencies())
print("Language is: ",country.languages())
print("Borders are: ",country.borders())
print("Other names: ",country.alt_spellings())

# Testing the script with Uganda country.
# Run it from terminal: python3 01_country_info_geography.py