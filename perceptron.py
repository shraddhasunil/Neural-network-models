import numpy as np
np.random.seed(0)

# XOR perceptron

class Perceptron(object):
    def __init__(self, eta=.5, b=0, w=np.random.rand(2)):
        self.eta = eta
        self.b = b
        self.w = w
    
    @staticmethod
    def step_function(x):
        if x<0:
            return 0
        else:
            return 1
        
   
    def train(self):
        training_set = [((0, 0), 0), ((0, 1), 1), ((1, 0), 1), ((1, 1), 1)]

        for i in range(len(training_set)):
            x1 = training_set[i][0][0]
            x2 = training_set[i][0][1] 
            y = training_set[i][1]

        errors = [] 
        for i in range(30):
            for x, y in training_set:
              #  print(x,w,self.b)
                u = sum(x*self.w) + self.b
               # print('u',u)
                error = y - Perceptron.step_function(u) 
                errors.append(error) 
                for index, value in enumerate(x):
               #     print(index,value,x)
                    self.w[index] += self.eta * error * value
                    self.b += self.eta*error
  
    def test(self,test_data):
        for test in (test_data):
            a = sum(test*self.w) + self.b
            print(a)
            predicted_y = Perceptron.step_function(a)
            print(predicted_y)

   
       
            
if __name__ == '__main__':
    p=Perceptron()
    p.train()
    test_data = [(0,1),(1,0),(1,1),(0,0)]
    p.test(test_data)
