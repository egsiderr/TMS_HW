from time import sleep

a = int(input("Enter value "))

def cycle_of_numbers(a):
    counter = 0
    while True:
        counter = (counter % a) + 1
        yield counter


for el in cycle_of_numbers(a):
    print(el)
    sleep(0.2)