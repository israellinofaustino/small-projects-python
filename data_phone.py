import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone

phone_number = phonenumbers.parse("+4401122334455")
# this will print the country name
print(geocoder.description_for_number(phone_number, 'en'))
# isso imprimirá o nome do provedor de serviço
print(carrier.name_for_number(phone_number, 'en'))
# this will print the time zone
print(timezone.time_zones_for_number(phone_number))