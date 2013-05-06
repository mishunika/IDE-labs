# -*- coding: utf-8 -*-
import sys
from calculator_brain import calculator_brain
from calculator_ui import Ui_Calculator
from PySide import QtGui

class CalculatorWindow(QtGui.QMainWindow):
  lcd_str = ''
  next_op = False
  two_operands = ['+', '-', u'×', u'÷']
  one_operand = [u'√', u'x²', u'±']
  def __init__(self, parent=None):
    super(CalculatorWindow, self).__init__(parent)
    self.ui = Ui_Calculator()
    self.ui.setupUi(self)
    self.bind_all()
    self.brain = calculator_brain()

  def update_lcd(self):
    if self.lcd_str[-2:] == '.0':
      self.lcd_str = self.lcd_str[:-2]
    self.ui.label.setText(self.lcd_str)

  def number_clicked(self):
    if self.next_op:
      self.next_op = False
      self.lcd_str = ''
      self.result = 0

    sender = self.sender()
    text = sender.text()
    if text == '.' and self.lcd_str.find('.') != -1:
      return

    self.lcd_str = self.lcd_str + text
    self.update_lcd()

  def operation_clicked(self):
    operation = self.sender().text()
    self.next_op = True
    if operation in self.two_operands:
      if self.brain.operand1 == 0:
        self.brain.operand1 = float(self.lcd_str)
      else:
        self.brain.operand2 = float(self.lcd_str)
        self.brain.perform_operation()
        self.lcd_str = str(self.brain.result)
      self.brain.operation = operation
    elif operation in self.one_operand:
      self.brain.operand1 = float(self.lcd_str)
      self.brain.operation = operation
      self.brain.perform_operation()
      self.lcd_str = str(self.brain.result)
    elif operation == '=':
      self.brain.operand2 = float(self.lcd_str)
      self.brain.perform_operation()
      self.lcd_str = str(self.brain.result)
    elif operation == 'C':
      self.brain.reset()
      self.lcd_str = '0'

    self.update_lcd()

  def bind_all(self):
    # Binding operand's buttons
    self.ui.pushButton_0.clicked.connect(self.number_clicked)
    self.ui.pushButton_1.clicked.connect(self.number_clicked)
    self.ui.pushButton_2.clicked.connect(self.number_clicked)
    self.ui.pushButton_3.clicked.connect(self.number_clicked)
    self.ui.pushButton_4.clicked.connect(self.number_clicked)
    self.ui.pushButton_5.clicked.connect(self.number_clicked)
    self.ui.pushButton_6.clicked.connect(self.number_clicked)
    self.ui.pushButton_7.clicked.connect(self.number_clicked)
    self.ui.pushButton_8.clicked.connect(self.number_clicked)
    self.ui.pushButton_9.clicked.connect(self.number_clicked)
    self.ui.pushButton_dot.clicked.connect(self.number_clicked)

    # Binding operation's buttons
    self.ui.pushButton_add.clicked.connect(self.operation_clicked)
    self.ui.pushButton_sub.clicked.connect(self.operation_clicked)
    self.ui.pushButton_mul.clicked.connect(self.operation_clicked)
    self.ui.pushButton_div.clicked.connect(self.operation_clicked)
    self.ui.pushButton_sqr.clicked.connect(self.operation_clicked)
    self.ui.pushButton_sqrt.clicked.connect(self.operation_clicked)
    self.ui.pushButton_sign.clicked.connect(self.operation_clicked)
    self.ui.pushButton_clear.clicked.connect(self.operation_clicked)
    self.ui.pushButton_equal.clicked.connect(self.operation_clicked)


if __name__ == "__main__":
  application = QtGui.QApplication(sys.argv)
  calculator = CalculatorWindow()
  calculator.show()
  sys.exit(application.exec_())
