# Section One: official QuickStart

>In gRPC a client application can directly call methods on a server application on a different machine as if it was a local object, making it easier for you to create distributed applications and services. As in many RPC systems, gRPC is based around the idea of defining a service, specifying the methods that can be called remotely with their parameters and return types. On the server side, the server implements this interface and runs a gRPC server to handle client calls. On the client side, the client has a stub (referred to as just a client in some languages) that provides the same methods as the server.

## For more detail: https://grpc.io/docs/guides/

- [proto3 Lnaguage Guide](https://developers.google.com/protocol-buffers/docs/proto3)

- [Python Generated Code](https://developers.google.com/protocol-buffers/docs/reference/python-generated)

- [grpc basic tutorial](https://grpc.io/docs/tutorials/basic/python.html)

- :)

## Install(python3/ubuntu)

```
pip install grpcio
pip install grpcio-tools googleapis-common-protos
```

## Example Code

```
# proto3 buffer 常用数据类型定义及 Python API 示例
data_type_parse_serialize_example.py
datatype_pb2.py

# grpc 示例
greeter_server.py
greeter_client.py
helloworld_pb2.py
helloworld_pb2_grpc.py
```

此 repo 中有些不完整的示例, 但有助于快速开始的.md .py .proto :)

# Section Two: Almost all data type(daily need).

example .proto in proto directory.
