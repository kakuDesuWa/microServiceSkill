# -*- coding:utf-8 -*-

import grpc

import auth_pb2, auth_pb2_grpc


def example(host='localhost:9000'):
    def client():
        channel = grpc.insecure_channel(host)
        stub = auth_pb2_grpc.ValidTokenStub(channel)

        response = stub.valid(auth_pb2.Token(token='123456'))
        print(response.is_valid)
        print(response.user_id)
        print(response.user_name)
    return client


if __name__ == '__main__':
    example()()
