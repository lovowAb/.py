"""
    Abdullahi
    lovowAb
"""
import re     # regular expressions
my_phone = "+20-115-926-3089" # Your Phone number
number = re.sub(r"#.*$, " ", my_phone)
print ("Your Phone number is: ", number)
number = re.sub(r"\D", " ", my_phone)
print ("Your Phone number without character is: ", number) 
