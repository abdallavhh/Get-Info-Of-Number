import phonenumbers as pn
from phonenumbers import carrier, geocoder, timezone

mobilenumber = input("Enter Phone Number With Country Code (+xx xxxxxxxx): ")
mobilenumber = pn.parse(mobilenumber)
if pn.is_valid_number(mobilenumber):
    print("Phone Number belongs to region: ", timezone.time_zones_for_number(mobilenumber))
    print("Service Provider: ",carrier.name_for_number(mobilenumber, "en"))
    print("Phone Number belongs to country: ", geocoder.description_for_number(mobilenumber, "en"))

else:
    print("Please Enter  a valid Phone Number.")