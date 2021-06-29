from sly import Parser
from lexer_2048 import MyLexer
import sys

class MyParser(Parser):
	tokens = MyLexer.tokens

	def __init__(self):
		self.names = { }
		self.bool=True

	@_('expr')
	def statement(self, p):
		return (p.expr)
	@_('ADD UP FS')
	def expr(self,p):
		return ('add_up',p.ADD,p.UP)
	@_('ADD DOWN FS')
	def expr(self,p):
		return ('add_down',p.ADD,p.DOWN)
	@_('ADD LEFT FS')
	def expr(self,p):
		return ('add_left',p.ADD,p.LEFT)
	@_('ADD RIGHT FS')
	def expr(self,p):
		return ('add_right',p.ADD,p.RIGHT)
	@_('SUBTRACT UP FS')
	def expr(self,P):
		return ('sub_up',P.SUBTRACT,P.UP)
	@_('SUBTRACT DOWN FS')
	def expr(self,P):
		return ('sub_down',P.SUBTRACT,P.DOWN)
	@_('SUBTRACT LEFT FS')
	def expr(self,P):
		return ('sub_left',P.SUBTRACT,P.LEFT)
	@_('SUBTRACT RIGHT FS')
	def expr(self,P):
		return ('sub_right',P.SUBTRACT,P.RIGHT)
	@_('MULTIPLY UP FS')
	def expr(self,P):
		return ('mult_up',P.MULTIPLY,P.UP)
	@_('MULTIPLY DOWN FS')
	def expr(self,P):
		return ('mult_down',P.MULTIPLY,P.DOWN)
	@_('MULTIPLY LEFT FS')
	def expr(self,P):
		return ('mult_left',P.MULTIPLY,P.LEFT)
	@_('MULTIPLY RIGHT FS')
	def expr(self,P):
		return ('mult_right',P.MULTIPLY,P.RIGHT)
	@_('DIVIDE UP FS')
	def expr(self,P):
		return ('div_up',P.DIVIDE,P.UP)
	@_('DIVIDE DOWN FS')
	def expr(self,P):
		return ('div_down',P.DIVIDE,P.DOWN)
	@_('DIVIDE LEFT FS')
	def expr(self,P):
		return ('div_left',P.DIVIDE,P.LEFT)
	@_('DIVIDE RIGHT FS')
	def expr(self,P):
		return ('div_right',P.DIVIDE,P.RIGHT)
	@_('ASSIGN NUMBER TO NUMBER COMMA NUMBER FS')
	def expr(self,P):
		return ('assign',P.NUMBER0,P.NUMBER1,P.NUMBER2)
	@_('VAR NAME IS NUMBER COMMA NUMBER FS')
	def expr(self,P):
		return ('var',P.NAME,P.NUMBER0,P.NUMBER1)
	@_('VALUE IN NUMBER COMMA NUMBER FS')
	def expr(self,P):
		return ('value',P.NUMBER0,P.NUMBER1)

	@_('NUMBER')
	def expr(self, p):
		return int(p.NUMBER)

	@_('NAME')
	def expr(self, p):
		print(f'Undefined name {p.NAME!r}')
		if self.bool==True:
			print('-1',file=sys.stderr)
			self.bool=False
	 
	@_('')
	def statement(self, p):
		pass
	@_('TRASH')
	def statement(self,p):
		if self.bool==True:
			print('-1',file=sys.stderr)
			self.bool=False

	def error(self,p):
		print("Syntax Error")
		if self.bool==True:
			print('-1',file=sys.stderr)
			self.bool=False
		
		