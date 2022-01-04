import time

class FiboIter():
    """
    This class generates an Iterator with the Fibonacci sequence. 
    
    Parameters:
        max: Max value of the sequence
    Returns:
        Returns the fibonacci sequence up to the max value defined in the max parameter
    """

    def __init__(self, max = 1):
        self.max = max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):

        if self.n1 + self.n2 <= self.max:
            if self.counter == 0:
                self.counter += 1
                return self.n1

            elif self.counter == 1:
                self.counter += 1
                return self.n2

            else:
                self.aux = self.n1 + self.n2
                # self.n1 = self.n2
                # self.n2 = self.aux
                #We can do a Swapping, replacing the two lines before with de next line of code
                self.n1, self.n2 = self.n2, self.aux
                self.counter += 1
                return self.aux
        else:
            raise StopIteration


def run():
    fibonacci = FiboIter()
    for element in fibonacci:
        print(element)
        time.sleep(0.05)

if __name__ == "__main__":
    run()