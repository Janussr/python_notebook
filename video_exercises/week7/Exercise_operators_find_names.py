import re
with open('addresses.txt') as f:
    addresses = f.read()

#print(addresses)

name = re.compile

phone_num_reg = re.compile(r'\d{2} \d{2} \d{2} \d{2}')
phone_number = phone_num_reg.findall(addresses)

zipcode = re.compile(r'\d{4}')
all_zipcodes = zipcode.findall(addresses)


zip_city = re.compile(r'\d{4} \w+')
zipcodes_and_cities = zip_city.findall(addresses)



#print(phone_number)
#print(all_zipcodes)
print(zipcodes_and_cities)
