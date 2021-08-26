from datetime import datetime


def decorator(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        elapsed_time = final_time - initial_time
        print(elapsed_time.total_seconds(),'have elapsed')
    
    return wrapper

@decorator
def suma(a,b,c = 1000000):
    for _ in range(c):
        a + b
if __name__ == '__main__':
    suma(5,485,100000000)
