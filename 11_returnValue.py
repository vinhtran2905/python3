def return_allowed_dateing_date(my_age):
    girls_age = my_age/2 + 7
    return girls_age

buckys_limit = return_allowed_dateing_date(27)

david_limit  = return_allowed_dateing_date(49)
print("Bucky cam date girls ", buckys_limit, " or older")
print("my limit is ", david_limit, " or older")