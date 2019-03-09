# summarized from 

    - [Language Guide proto3](https://developers.google.com/protocol-buffers/docs/proto3)
    - [Python Generated Code](https://developers.google.com/protocol-buffers/docs/reference/python-generated)

前者讲述 proto3 中, 对各种基本数据类型的定义, 及一些数据类型定义的"套路"...

后者结合 Python 示例给出根据定义的(proto buffer) parsing from and serializing to binary strings.

## basic data type

Note: 
    1. 下指对应的 Python3 类型
    2. 这里给出的并不全, 更详细, 参考文档

- string

    ```
    message StringMessage {
        string string_field = 1;
    }
    ```
- bytes

    ```
    message BytesMessage {
        bytes bytes_field = 1;
    }
    ```

- bool

    ```
    message BoolMessage {
        bool bool_field = 1;
    }
    ```

- int

    ```
    // int32 int64 uint32 uint64 sint32 sint64 fixed32 fixed64 sfixed32 sfix64
    message IntMessage {
        int32 int_field = 1;
    }
    ```

- float

    ```
    // float double
    message FloatMessage {
        float float_field = 1;
    }
    ```

- list

    ```
    // array
    message ListIntMessage {
        repeat int int_field = 1;
    }
    // list of string
    message ListStringMessage {
        repeat string string_field = 1;
    }
    ```

- dict

    ```
    message DictMessage {
        map<int32, string> dict_filed = 1;
    }
    ```
