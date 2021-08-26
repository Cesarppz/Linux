import time

class Iterator():
    def __init__(self,max=None):
        self.max = max - 1


    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.count = 0
        return self
    

    def __next__(self):
        if self.max is None or self.count <= self.max:
            if self.count == 0:
                self.count += 1
                return self.n1

            elif self.count == 1:
                self.count += 1
                return self.n2

            else:
                self.count += 1
                self.sum = self.n1 + self.n2
                self.n1, self.n2 = self.n2, self.sum
                return self.sum
        else:
            raise StopIteration


if __name__ == '__main__':
    fivonacci = Iterator(max=100)
    for number in fivonacci:
        print(number)
        time.sleep(0.5)