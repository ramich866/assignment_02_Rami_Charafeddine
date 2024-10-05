# Ex1:

def getFactorial(s):
 factorial_number = 1 
 for i in range(1, s+1):
   factorial_number *= i
 return factorial_number

n =int(input("please enter a number"))
print(getFactorial(n))


# Ex2:

def find_divisors():
  n = int(input("please enter a number: "))

  listDiv = []

  for i in range(1, n+1):
    if (n % i == 0): 
      listDiv.append(i)
           
  return listDiv

print(find_divisors())


#Ex3:

def reverseString(s):
  reversed_str = ""

  for word in s:
    reversed_str = word + reversed_str

  return reversed_str

user = input("please enter any word:")
print("Reversed string: ", reverseString(user))


#Ex4:

def getEven():

  list_integers = []

  n = int(input("how many integers you want: "))

  for i in range(n):
    integer = int(input("what is the integer you want to add: "))
    list_integers.append(integer)

  even_list = []

  for integer in list_integers:
    if (integer % 2 == 0): 
      even_list.append(integer)
  
  return even_list

print(getEven())


#Ex5:

def is_strong_password(p):
  
  hasUpper = False
  hasLower = False
  hasDigit = False
  hasSpecial = False
  specialCharacters = "#?!$"

  for char in p:
    if 'A' <= char <='Z':
      hasUpper = True
    elif 'a' <= char <= 'z':
      hasLower = True
    elif '0' <= char <= '9':
      hasDigit = True
    elif char in specialCharacters:
      hasSpecial = True 

  if len(password) >= 8 and hasUpper and hasLower and hasDigit and hasSpecial:
    return "Strong password"
  else:
    return "Weak password"

password=input("please enter an password: ")
print(is_strong_password(password))  


#Ex6:

def is_valid_ipv4_address(ip):
    
    parts = ip.split('.')
    
    if len(parts) != 4:
        return "invalid IPv4 addresses"
    
    for part in parts:
        if not part.isdigit() or (part[0] == '0' and len(part) > 1):
            return "invalid IPv4 address"
        
        num = int(part)
        if num < 0 or num > 255:
            return "invalid IPv4 address"
    
    return "valid IPv4 address"
ipAddresses = input("please enter an IP address")
print(is_valid_ipv4_address(ipAddresses))
