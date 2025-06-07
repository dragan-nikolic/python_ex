def logical_or(op1, op2):
    result = op1
    #if not result or result == '':
    if not result:
        result = op2
    print(result)

logical_or('operand1', 'operand2')
logical_or('', 'EmptyOrOperand2')
logical_or(None, 'NoneOrOperand2')
logical_or(True, 'TrueOrOperand2')
logical_or(False, 'FalseOrOperand2')
