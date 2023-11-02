import time
import os
import matplotlib.pyplot as plt

class Random:
    
    def __init__(self, seed=None, weight=1664525, bias=1013904223, m=2**23) -> None:
        self.__weight = weight
        self.__bias = bias
        self.__m = m
        
        if seed is None:
            self.x0 = time.time() + 30000*os.getpid() + 12345678
        else:
            self.x0 = seed
    
        self.__x1 = (self.__weight*self.x0 + self.__bias) % self.__m
        
    def randint(self, range=None) -> int:
        self.__x1 = (self.__weight*self.__x1 + self.__bias) % self.__m
        
        if range is None:
            return self.__x1
        else:
            scalar = self.__x1 / (self.__m - 1)
            return int(scalar*(range[-1] - range[0]) + range[0])
        
    def rand(self, range=None) -> int:
        self.__x1 = (self.__weight*self.__x1 + self.__bias) % self.__m
        
        if range is None:
            return self.__x1
        else:
            scalar = self.__x1 / (self.__m - 1)
            return scalar*(range[-1] - range[0]) + range[0]
    
if __name__ == '__main__':
    
    def testRandomInt():
        random_generator = Random()
        
        ls = []
        for i in range(0, 100001):
            ls.append(random_generator.randint([1, 101]))
        
        ref = [n for n in range(1, 101)]
        element_counts = {num: ls.count(num) for num in ref}
        
        ls_len = len(ls)
        
        # for num, count in element_counts.items():
        #     print(f"Frequent of {num:>3}: {count:>6} || Probability of it: {100 * count / ls_len:>10.6f}%")
    
        probabilities = [100*count / ls_len for num, count in element_counts.items()]
    
        plt.figure(num='Figure 1', figsize=(6, 6))
        plt.plot(ref, probabilities)
        plt.xlabel('Random number')
        plt.ylabel('Probability (%)')
        plt.title('Probability Desity Function')
        plt.grid(True)
        plt.show()

    testRandomInt()