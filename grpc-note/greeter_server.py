import time
from concurrent import futures
import grpc

from grpc_codes import helloworld_pb2, helloworld_pb2_grpc


class Greeter(helloworld_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        print('Server-end...')
        print('First argument request')
        print(request, type(request))
        print('second argument *context*')
        print(context, type(context))
        print('[detail] request.name=> %s' % request.name)
        return helloworld_pb2.HelloReply(message='reply from server-end')

    def Kakumethod(self, request, context):
        print('Server-end...')
        print('First argument request')
        print(request, type(request), request)
        print('second argument *context*')
        print(context, type(context), context)
        print('[detail] request.name=> %s' % request.message)
        return helloworld_pb2.KakuResponse(
            response=['response from server-end 1',
                      'response from server-end 1'],
            msg=1,
        )


def run_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(600)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    run_server()
