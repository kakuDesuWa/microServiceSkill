import grpc

from grpc_codes import helloworld_pb2, helloworld_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = helloworld_pb2_grpc.GreeterStub(channel)

    response = stub.SayHello(helloworld_pb2.HelloRequest(name='kaku'))
    print('I: Client-end...')
    print('I: receive response:')
    print(response)
    print('I: receive response.message:')
    print(response.message, type(response.message))

    print('\n===== *another* =====\n')

    response2 = stub.Kakumethod(
        helloworld_pb2.KakuRequest(
            message=['message1', 'message2']
        )
    )
    print('I: Client-end...')
    print('I: receive response2:')
    print(response2)
    print('I: receive response2.response')
    print(response2.response, type(response2.response))
    print('I: receive response2.msg')
    print(response2.msg, type(response2.msg))


if __name__ == '__main__':
    run()

