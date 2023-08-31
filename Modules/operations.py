import operator

def get_operator(op):
	return {
		'+' : operator.add,
		'-' : operator.sub,
		'x' : operator.mul,
		'divided' :operator.truediv,'by' :operator.truediv,
		}[op]

def Expression(op1, oper, op2):
	op1,op2 = int(op1), int(op2)
	return get_operator(oper)(op1,op2)