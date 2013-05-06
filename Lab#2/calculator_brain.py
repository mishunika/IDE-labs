# -*- coding: utf-8 -*-
import math

class calculator_brain:
  operand1 = 0
  operand2 = 0
  operation = ''
  result = 0

  def __init__(self):
    self.reset()

  def reset(self):
    self.operand1 = 0
    self.operand2 = 0
    self.operation = ''

  def perform_operation(self):
    operations = {
      '+' : self.add,
      '-' : self.sub,
      u'÷' : self.div,
      u'×' : self.mul,
      u'√' : self.sqrt,
      u'x²' : self.sqr,
      u'±' : self.sign
    }
    self.result = operations[self.operation]()
    self.reset()

  def add(self):
    return self.operand1 + self.operand2

  def sub(self):
    return self.operand1 - self.operand2

  def div(self):
    return self.operand1 / self.operand2

  def mul(self):
    return self.operand1 * self.operand2

  def sqrt(self):
    if self.operand1 < 0:
      return 0

    return math.sqrt(self.operand1)

  def sqr(self):
    return self.operand1**2

  def sign(self):
    return -1 * self.operand1


if __name__ == "__main__":
  ae = calculator_brain()
  ae.operand1 = 5.0
  ae.operand2 = 9.2
  ae.operation = '/'
  ae.perform_operation()

  print ae.result
