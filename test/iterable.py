# from collections import abc
#
#
# class IterableObject:
#     def __iter__(self):
#         cont = 0
#         while cont < 4:
#             cont += 1
#             yield cont
# a_it = IterableObject()
# assert isinstance(a_it, abc.Iterable)

class ProblemB(object):
    def __init__(self):
        # 初始化数列计数器
        self.count = 0
        self._length = 0

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if not isinstance(value, int):
            raise ValueError("length must be a integer!")
        if value < 1 or value > 100:
            raise ValueError("length must between 1 ~ 100!")
        self._length = value

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.length:
            raise StopIteration()
        self.count = self.count + 1
        self.value = self.count * 2 - 1
        return self.value


def solution(sample):
    solu_iter = ProblemB()
    solu_iter.length = sample
    sum = 0
    for i in solu_iter:
        sum += i
    return sum


print(solution(10))