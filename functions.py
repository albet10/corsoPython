#name = input('What is your name?') # User types "Kolade" and presses Enter  
#print('Hello', name) # Output: Hello Kolade

print(int(3.14)) # 3
print(int('42')) # 42
print(int(True)) # 1
print(int(False)) # 0 

def hello():
    print('Hello World')
hello();    

def calculate_sum(a, b):
    print(a + b)
calculate_sum(3, 1)

#none
def calculate_sum(a, b):
    print(a + b)
my_sum = calculate_sum(3, 1) # 4
print(my_sum) # None - perché il valore non è stato registrato. Cambiamo allora print con return
def calculate_sum(a, b):
    return (a + b)
my_sum = calculate_sum(3, 1) # 4
print(my_sum) # None

#SCOPE - global and local
tax_rate = 0.1

def calculate_tax(price):
    tax = price * tax_rate
    return tax

print(calculate_tax(50)) # 5.0
print(tax_rate) # 0.1
print(tax) # NameError: name 'tax' is not defined