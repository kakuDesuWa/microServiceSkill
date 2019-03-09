#! /usr/bin/env python3
# coding: utf-8
#
# author: kaku
# data: 18/07/14
#
# GitHub:
#
#   https://github.com/kakuchange
#
# proto buffer data type python parse and serialize example code.

from grpc_codes import datatype_pb2


def example():
    """parsing and serialize example.

    Notes:
        string
        bytes
        bool
        int
        float
        list
        dict
    """
    # 实例时, 不显示指定的field都有默认 "零值"

    # string
    string_msg = datatype_pb2.StringMessage(string_field='kaku')
    assert string_msg.string_field == 'kaku'

    # common method
    serialize_res = string_msg.SerializeToString()
    string_msg.Clear()
    string_msg.ParseFromString(serialize_res)

    # bytes
    bytes_msg = datatype_pb2.BytesMessage(bytes_field=b'kaku bytes type')
    assert bytes_msg.bytes_field == b'kaku bytes type'
    try:
        bytes_msg.bytes_field = 'kaku not bytes type'
    except TypeError:
        print('assign bytes type data please!')

    # bool
    bool_msg = datatype_pb2.BoolMessage(bool_field=True)
    assert bool_msg.bool_field == True

    # int
    # note: proto define int32
    int_msg = datatype_pb2.IntMessage(int_field=2 ** 10)
    assert int_msg.int_field == 2 ** 10

    # float
    float_msg = datatype_pb2.FloatMessage(float_field=1.0)
    assert float_msg.float_field == 1.0

    # list of int
    # list_of_int_msg = datatype_pb2.ListIntMessage(int_field=[1, 2, 3])
    list_of_int_msg = datatype_pb2.ListIntMessage()
    list_of_int_msg.int_field.append(1)
    try:
        list_of_int_msg.int_field.append(1.1)
    except TypeError:
        print('hihi :)')
    list_of_int_msg.int_field.extend([2, 3])
    assert list_of_int_msg.int_field == [1, 2, 3]

    # list of string
    list_of_str_msg = datatype_pb2.ListStringMessage(string_field=['a', 'b', 'c'])

    # dict of filed[int] => string
    # dict_msg = datatype_pb2.DictMessagei2s(dict_field={1: 'kaku', 2: 'Python'})
    dict_msg = datatype_pb2.DictMessagei2s()
    dict_msg.dict_field[1] = 'kaku'
    for k, v in dict_msg.dict_field.items():
        assert k == 1
        assert v == 'kaku'

    # dict of filed[string] => string
    # dict_msg = datatype_pb2.DictMessages2s(dict_field={'name': 'kaku', 'language': 'Python'})
    dict_msg = datatype_pb2.DictMessages2s()
    dict_msg.dict_field['name'] = 'kaku'
    for k, v in dict_msg.dict_field.items():
        assert k == 'name'
        assert v == 'kaku'


if __name__ == '__main__':
    example()

