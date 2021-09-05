import time 


def fivonacci_gen(max=100):
    num1 , num2 = 0, 1
    count = 0
    while count <= max - 1:
        yield num1
        num1, num2 = num2 , num1 + num2
        count += 1
    

if __name__ == '__main__':
    gen = fivonacci_gen(10)
    for number in gen:
        print(number)
        time.sleep(0.3)