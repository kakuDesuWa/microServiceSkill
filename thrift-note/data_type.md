# Summary from https://thrift-tutorial.readthedocs.io/en/latest/thrift-types.html

# Thrift type system

include base types like **bool, byte, double, string and integer** but also special types like **binary** and it also supports **structs**(equivalent to classes but without inheritance) and also **containers**(list, set, map) that correspond to commonly available in all programming languages and omits types that are specific to only some programming languages.

## Base types

- bool
- byte
- i16
- i32
- i64
- double
- string

Note: There is no support for unsigned integer types.

## Special  Types

- binary: a sequence of unencoded of bytes.

## Structs

A struct has a set of strongly typed fileds, each with a unique name identifier. The look very similar to C-like structs.

```
struct Example {
    1: i32 number=10,
    2: i64 bigNumber,
    3: double decimals,
    4: string name="thrifty",
}
```
## Containers

- list
- set
- map

## Exceptions

exception InvalidOperation {
    1: i32 what,
    2: string why
}

## Services

A service consists of a set of named function, each with a list of parameters and a return type. It is semantically equivalent to defining an interface or a pure virtual abstract class.

```
service <name> {
    <returntype> <name>(<arguments>) [throws (exceptions)]
    ...
}

An example:
service StringCache {
    void set(1:i32 key, 2:string value),
    string get(1:i32 key) throws (1:KeyNotFound knf),
    void delete(1: i32 key)
}
```

# Important Info, summary from proto/tutorial.thrift

- ```include "shared.thrift"``` means you can access shared.SharedObject in this .thrift that defined in another .thrift file.

- ```const i32 INT32CONSTANT = 1993``` thrift also let you define constants use across languages.

- or more complex ```const map<string, string> MAPCONSTANT = {"hello": "world", "name": "kaku"}``` types and structs are specified using JSON notation.

- enums you can define, which are just 32 bit integers. Values are optional and start at 1 if not supplied, C style again.
```
enum Operation {
    ADD = 1
    SUBTRACT = 2
    MULTIPLY = 3
    DIVIDE = 4
}
```

- Stucts are the basic complex data structures. They are comprised of fileds which each have an integer identifier, a type, a symbolic name, and an optional default value. you can define optional field. eg:

```
struct Work {
    1: i32 num1 = 0,
    2: i32 num2,
    3: Operation op,
    4: optional string comment,
}
```

- Structs can also be excetions, if they are nasty.

exception InvalidOperation {
    1: i32 whatOp,
    2: string why
}

- Define a service, Services just need a name and can optionally inherit from another service using the extends keywork. ```oneway``` method means only makes a request and does not listen for any response at all.

```
service Calculate extends shared.SharedService {
    void ping(),

    i32 add(1: i32 num1, 2: i32 num2),
    i32 calculate(1: i32 logid, 2: Work w) throws (1: InvalidOperation),
    oneway void zip()
}
```