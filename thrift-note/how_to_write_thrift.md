# Summary from https://thrift-tutorial.readthedocs.io/en/latest/thrift-file.html

# Writing a .thrift file

In a .thrift file you can define the services that your server will implement and that they will be called by andy clients. The Thrift compiler will read this file and generate source code to be used from the services and clients you will write.

A simple .thrift file with which we defined our simple multiplication service for this demo looks like this:

```
namespace java tutorial
namespace py tutorial

/*
 C like comments are supported
*/
// This is also a valid comment

// We can use typedef to get pretty names for the types we are using
typedef i32 int

service MultiplicationService {
    int multiply(1:int n1, 2:int n2),
}
```

In the above file we just define a service to multiply two numbers and return their product to avoid making our first demo hard to understand. If you named this file multiplication. thrift and you want to use java and python all you need to do is to run.

```
thrift --gen java multiplication.thrift
thrift --gen py multiplication.thrift
```

- Notice in the above file the namespaces we define. The dictate that Thrift should generate a sub-directory named tutorial inside gen-java and gen-py and place the output files there. We could have specified different namespaces for java and python. We could also omit specifying a namespace.In the latter case the files would be place directly inside the gen-java and gen-py directories.

- Notice also that we can typedef Thrift types with someting more easy to remember(i32 with int in this case)

You can find more detail in tutorial.thrift. Below we notice its most important parts.

## Include othe .thrift files

Included objects are accessed using the name of the .thrift file as a prefix. ie. shared.SharedObject

```
include "shared.thrift"
```

## Define C-style enumerations

Values are optional and start at 1 if not specified.

```
enum Operation {
  ADD = 1,
  SUBTRACT = 2,
  MULTIPLY = 3,
  DIVIDE = 4
}
```

## Define Sturcts

Fields can be declared "optional", which ensures they will not be included in the serialized output if they aren't set- This requires some manual management in some languages. Do you notice the numbers before each filed type? Fields identifiers is the way Thrift performs versioning. The Thrift definition language supports automatic assignment os filed identifiers, but it is good programming practice to always explicitlyu specify field identifiers. As explained in Thrift’s whitepaper To avoid conflicts between manually and automatically assigned identifiers, fields with identifiers omitted are assigned identifiers decrementing from -1, and the language only supports the manual assignment of positive identifiers.

```
struct Work {
    1: i32 num1=0,
    2: i32 num2=,
    3: Operation op,
    4: optional string comment,
}
```

## Define a Service

```
exception InvalidOperation {
  1: i32 what,
  2: string why
}
```

## Define Service

```
service Calculator extends shared.SharedService {
    void ping()

    i32 add(1: i32 num1, 2: i32 num2),

    i32 calculate(1: i32 logid, 2: work w) throw (1:Invalid),

   /**
    * This method has a oneway modifier. That means the client only makes
    * a request and does not listen for any response at all. Oneway methods
    * must be void.
    */
   oneway void zip()
}
```