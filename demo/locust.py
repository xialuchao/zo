# coding=utf-8
from locust import HttpLocust, TaskSet


def test1(self):
    r = self.client.get("/company/test", timeout=30)
    # 这里可以使用assert断言请求是否正确，也可以使用if判断
    assert r.status_code == 200
    print(r)

# class UserBehavior(TaskSet):
#     tasks = {
#         test: 1,
#     }


class WebsiteUser(HttpLocust):
    # task_set = UserBehavior
    host = "http://ft1.mobile.zhaoonline.com"
    min_wait = 3000
    max_wait = 6000