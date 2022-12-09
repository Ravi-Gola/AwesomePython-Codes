import phonenumbers
from phonenumbers import timezone,geocoder,carrier
num=input("enter your number with country code eg india : +91 ")
phone=phonenumbers.parse(num)
time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone,"en")
reg=geocoder.description_for_number(phone,"en")
print(phone,"and",time,"and",car,"and",reg)