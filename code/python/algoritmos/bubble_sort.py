import random


def chanche_idx(n1,n2,array):
    temp = array[n1]
    array[n1] = array[n2]
    array[n2] = temp
    return array


def run(array):

    for _ in range(len(array)-1):

        for i in range(len(array)-1):
            print(array[i])
            if array[i] > array[i+1]:
                array = chanche_idx(i,i+1,array)
                print(array)
            
    print(f'Oedenada {array}')


if __name__ == '__main__':
    n = int(input('De cuanto quieres el array? '))
    array = [random.randint(0,100) for i in range(n)]
    print(f'Lista desordenada{array}\n')
    run(array)