import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
install('sly')

from lexer_2048 import MyLexer
from parser_2048 import MyParser
from execute_2048 import MyExecute
import sys

def main():
	lexer = MyLexer()
	env = {}
	while True:
		try:
			print("2048>",end="")
			text = input()
		 # The entry point to the parser
		# print(parser.last_item_on_stack)
		except EOFError:
			break
		if text :
			tokens = lexer.tokenize(text) # Creates a generator of tokens
			#for tok in tokens:
			#	print(tok)
			parser = MyParser()
			tree=parser.parse(tokens) 
			basic_execute=MyExecute(tree,env)


if __name__ == '__main__':
	main()
