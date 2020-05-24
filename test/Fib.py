# def fab(max):
#     n,a,b=0,1,1
#     fib = []
#     while n<max:
#         fib.append(b)
#         a,b = b, a+b
#         n = n+1
#     print(fib)
#     return fib
# fab(5)

# class Fab:
#     def __init__(self, max):
#         self._max = max
#         self.n,self.a,self.b = 0,0,1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.n < self._max:
#             r = self.b
#             self.a, self.b = self.b, self.a + self.b
#             self.n = self.n+1
#             return r
#         raise StopIteration()
# for n in Fab(5):
#     print(n)

def fab(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n += 1
fab(3)

