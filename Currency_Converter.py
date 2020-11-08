with open('data.txt') as f:
    lines = f.readlines()
 
currency_dict = {} 
for line in lines:
    parsed = line.split('\t')
    currency_dict[parsed[0]] = parsed[1]
    
amount = int(input("Enter the amount:"))
[print(currencies) for currencies in currency_dict.keys()]
print("\nChoose in which currency do you want to convert your amount.\n")
currency = input(":")
print(f"{amount} in INR is {amount * float(currency_dict[currency])} in {currency}.")
