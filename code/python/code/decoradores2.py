from datetime import datetime


def decorator(func):
    def wrapper(*args, **kwargs):
        #initial_time = datetime.now()
        print(func(*args, **kwargs))
        #final_time = datetime.now()
        #elapsed_time = final_time - initial_time
       # print(elapsed_time.total_seconds(),'have elapsed')
    
    return wrapper

@decorator
def suma(a,b,c ):
    return a,b,c
    # for _ in range(1,c):
    #     print(a)
if __name__ == '__main__':
    suma(5,485,1000)
