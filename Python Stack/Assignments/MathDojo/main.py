class MathDojo:
    def __init__(self):
        self.result=0
        
    def add(self,num,*nums):

        self.result+=num
        for n in nums:

            self.result+=n
        return self
    
    
    def subtract(self,num,*nums):

        self.result-=num
        for n in nums:

            self.result-=n
        return self


md = MathDojo()
x = md.add(10).add(15, 5).add(10, 20, 30).result
print(x) 


md = MathDojo()
y = md.add(2).add(2, 5, 1).subtract(3, 2 , 1).result
print(y) 

md = MathDojo()
z = md.subtract(10).subtract(20, 5,10).subtract(6, 5, 9).result
print(z)

md = MathDojo()
w = md.add(50, 25).subtract(20, 10).add(8,7).add(20).result
print(w)  
