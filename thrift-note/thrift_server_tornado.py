#! /usr/bin/env python3
# coding: utf-8
#
# author: kaku
# date: 18/09/07
#
# GitHub:
#
#   https://github.com/kakuchange
#
# Description:
#
#   thrift with tornado.
#   copy from: https://github.com/apache/thrift

import glob
import sys

sys.path.append('gen-py.tornado')
# sys.path.insert(0, glob.glob('../../lib/py/build/lib*')[0])

from tutorial import Calculator
from tutorial.ttypes import Operation, InvalidOperation

from shared.ttypes import SharedStruct

from thrift import TTornado
from thrift.protocol import TBinaryProtocol

from tornado import ioloop


class CalculatorHandler(object):
    def __init__(self):
        self.log = {}

    def ping(self):
        print("ping()")

    def add(self, n1, n2):
        print("add({}, {})".format(n1, n2))
        return n1 + n2

    def calculate(self, logid, work):
        print("calculate({}, {})".format(logid, work))

        if work.op == Operation.ADD:
            val = work.num1 + work.num2
        elif work.op == Operation.SUBTRACT:
            val = work.num1 - work.num2
        elif work.op == Operation.MULTIPLY:
            val = work.num1 * work.num2
        elif work.op == Operation.DIVIDE:
            if work.num2 == 0:
                x = InvalidOperation()
                x.whatOp = work.op
                x.why = "Cannot divide by 0"
                raise x
            val = work.num1 / work.num2
        else:
            x = InvalidOperation()
            x.whatOp = work.op
            x.why = "Invalid operation"
            raise x

        log = SharedStruct()
        log.key = logid
        log.value = '%d' % (val)
        self.log[logid] = log
        return val

    def getStruct(self, key):
        print("getStruct({})".format(key))
        return self.log[key]

    def zip(self):
        print("zip()")


def main():
    handler = CalculatorHandler()
    processor = Calculator.Processor(handler)
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()
    server = TTornado.TTornadoServer(processor, pfactory)

    print("Starting the server...")
    server.bind(9090)
    server.start(1)
    ioloop.IOLoop.instance().start()
    print("done.")


if __name__ == "__main__":
    main()
