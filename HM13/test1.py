from time import sleep

a = int(input("Enter value "))

def fibonachi_gen(a,):
    val1 = 1
    val2 = 2
    counter = 0

    while counter < a:
        counter += 1

        val1, val2 = val2, val1 + val2

        yield val2

for el in fibonachi_gen(a):
    print(el)
    sleep(0.2)