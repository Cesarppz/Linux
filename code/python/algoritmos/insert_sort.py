import random

def run(array):
    for i in range(len(array)):
        position = i

        while position >0 and array[position - 1] > array[position]:
            temp = array[position - 1]
            array[position - 1] = array[position]
            array[position] = temp

            position -= 1 

    print(array)



if __name__ == '__main__':
    n = int(input('De cuanto quieres el array? '))
    array = [random.randint(0,100) for i in range(n)]
    print(f'Lista desordenada{array}\n')
    run(array)