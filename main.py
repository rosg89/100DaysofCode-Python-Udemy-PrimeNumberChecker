#Write your code below this line 👇

#Numeros primos: Solo se dividen por si mismos y por 1

def prime_checker(number):
  is_prime = True 
  for i in range(2, number):
    if number % i == 0:
    #Si es divisible entre por 2 o el numero anterior a number, no es primo
      is_prime = False
  if is_prime == True:
    print("It is a prime number.")
  else:
    print("It's not a prime number.")
      



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



