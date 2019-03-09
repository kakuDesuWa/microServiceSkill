import time

from locust import Locust, TaskSet, events, task

from auth_client import example


class GRpcClient:

    def __init__(self, host):
        self.host = host

    def __getattr__(self, name):
        func = example(self.host)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                total_time = int((time.time() - start_time) * 1000)
                events.request_failure.fire(
                    request_type="grpc",
                    name=name,
                    response_time=total_time,
                    exception=e,
                )
            else:
                total_time = int((time.time() - start_time) * 1000)
                events.request_success.fire(
                    request_type="grpc",
                    name=name,
                    response_time=total_time,
                    response_length=0,
                )
                # In this example, I've hardcoded response_length=0. If we would want the response length to be
                # reported correctly in the statistics, we would probably need to hook in at a lower level
        return wrapper

class GRpcLocust(Locust):
    def __init__(self, *args, **kwargs):
        super(GRpcLocust, self).__init__(*args, **kwargs)
        self.client = GRpcClient(self.host)


class ApiUser(GRpcLocust):

    host = "localhost:9000"
    min_wait = 100
    max_wait = 1000

    class task_set(TaskSet):
        @task(10)
        def name_whatever(self):
            self.client.name_whatever()
