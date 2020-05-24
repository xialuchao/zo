# import time
# from threading import Thread
# import threading
#
# start = time.clock()
# def CountDown(n):
#     while n>0:
#         print(threading.current_thread().getName())
#         n -= 1
#
# t1 = Thread(target=CountDown, args=[100000])
# t2 = Thread(target=CountDown, args=[100000])
# t1.start()
# t2.start()
# t1.join()
# t2.join()
#
# print(time.clock()-start)


# #单例 e
# class Singleton(object):
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(Singleton, '_instance'):
#             cls._instance = super(Singleton, cls).__new__()
#         return cls._instance
#
#     @classmethod
#     def get_instance(cls):
#         return cls._instance
#
#     @classmethod
#     def sum(cls, num1, num2):
#         print(Singleton._instance)
#         return num1+num2
#
#     @staticmethod
#     def reduce(num1, num2):
#         print(Singleton._instance)
#         return num1-num2
#
# #懒汉(线程不安全）
#
# class Singleton1(object):
#     _instance = None
#
#     def __init__(self):
#         if not hasattr(Singleton1, '_instance'):
#             print("__init__ method called but no instance created")
#         else:
#             print("instance already created:", self._instance)
#
#     @classmethod
#     def get_instance(cls):
#         if not cls._instance:
#             cls._instance = Singleton1()
#         return cls._instance
#
# # synchronized
# import threading
# def synchronized(func):
#     func.__lock__ = threading.Lock()
#
#     def lock_func(*args, **kwargs):
#         with func.__lock__:
#             return func(*args, **kwargs)
#     return lock_func
#
# class Singleton2(object):
#     instance = None
#
#     @synchronized
#     def __new__(cls, *args, **kwargs):
#         if cls.instance is None:
#             cls.instance = super().__new__(cls)
#         return cls.instance
#
#     def __init__(self, num):
#         self.a = num + 5

# #fixture
# import pytest
# # def test1(before):
# #     print(1)
# #
# # def test2(before):
# #     print(2)
# #     assert 0
#
# # pytestmark=pytest.mark.usefixtures("before")
# # @pytest.fixture(autouse="true")
#
#
# class Test_fix():
#     # @pytest.mark.userfixtures("before")
#     @pytest.mark.aaa
#     def test1(self):
#         print(1)
#         assert 1 == 1
#
#     # @pytest.mark.userfixtures("before")
#     def test2(self):
#         print(2)
#         assert 2 == 2
#
#
#
# if __name__ == "__main__":
# #     pytest.main(["-m", "aaa","-s", "test.py"])
#
# a = [{
#   "mobile_id": "942bbbd3",
#   "mobile_version": "9",
#   "mobile_model": "OPPO PAFM00",
#   "mobile_resolution": "2340 x 1080"
#  },{
#   "mobile_id": "942bdddbd3",
#   "mobile_version": "9",
#   "mobile_model": "OPPO PAFM00",
#   "mobile_resolution": "2340 x 1080"
#  }]
#
# # print(len(a[0]))
# # print(a[1]["mobile_id"])
#
# for i in range(len(a)):
#     print(a[i]["mobile_id"])




a = "abd"
print(url +"/"+ a)
