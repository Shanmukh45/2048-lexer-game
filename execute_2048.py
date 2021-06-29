import game_funcs
from collections import defaultdict
import sys
import numpy as np

class driver():
    def __init__(self):
        self.commands = ["a","w","d","s"]
        self.init_matrix()
        self.curr=True
        self.names=np.array([["" for _ in range(4)] for _ in range(4)],dtype='object')
        #print(self.names)
       # print(len(self.names))
        
    def init_matrix(self):
        self.matrix = game_funcs.start_game()

    def draw_matrix(self):
        print('Current Matrix is:')
        for i in range(4):
            for j in range(4):
                print(self.matrix[i][j],end=" ")
            print("")
        print("")
    
    def key_press(self,key,op):
        if key in self.commands:
           # print(self.names)
            x=key
            if(x=="w" or x=="W"):
                self.matrix, move_made, sc,self.names= game_funcs.move_up(self.matrix,op,self.names)
            if(x=="s" or x=="S"):
                self.matrix, move_made, sc ,self.names = game_funcs.move_down(self.matrix,op,self.names)
            if(x=="A" or x=="a"):
                self.matrix, move_made, sc ,self.names= game_funcs.move_left(self.matrix,op,self.names)
            if(x=="d" or x=="D"):
                self.matrix, move_made, sc ,self.names= game_funcs.move_right(self.matrix,op,self.names)
            if move_made:
                self.matrix = game_funcs.add_new_tile(self.matrix)
                move_made = False
           # print(self.names)
        self.draw_matrix()
        
    def key_press_2(self,p,q,num):
        if p>3 or q>3:
            print("Out of Bounds")
            return
        else:
            game_funcs.add_num_tile(self.matrix,p,q,num)
            print('Value added')
            self.draw_matrix()

    def key_press_3(self,p,q):
        if p>3 or q>3:
            print("Out of Bounds")
            return
        print(game_funcs.what_value(self.matrix,p,q))

    def key_press_4(self,p,q,name):
        #print(p,q,name)
        self.names[p][q]=self.names[p][q]+name

Driver=driver()
Driver.draw_matrix()

class MyExecute:
    
    def __init__(self, tree, env):
        self.env = env
        self.bool=True
        if not any(0 in row for row in Driver.matrix) and not game_funcs.horizontal_move_exists(Driver.matrix) and not game_funcs.vertical_move_exists(Driver.matrix):
            Driver.draw_matrix()
            print("Game Over")
            print("Thank you for playing the game")
            exit()
        result = self.walkTree(tree)
        if self.bool==False:
            #print("It's true")
            for i in range(4):
                for j in range(4):
                    print(Driver.matrix[i][j],end=" ",file=sys.stderr)
            for i in range(4):
                for j in range(4):
                    if len(Driver.names[i][j])!=0:
                        g=str(i)
                        f=str(j)
                        h=''
                        for m in range(len(Driver.names[i][j])):
                            h=h+Driver.names[i][j][m]
                        print(g+','+f+h,end=" ",file=sys.stderr)
            print("",file=sys.stderr)
        if result is not None and isinstance(result, int):
            print(result)
        if isinstance(result, str) and result[0] == '"':
            print(result)
       # print("hey")

    def walkTree(self, node):
  
        if isinstance(node, int):
            return node
        if isinstance(node, str):
            return node
  
        if node is None:
            return None
  
        if node[0] == 'num':
            return node[1]
  
        if node[0] == 'str':
            return node[1]
  
        if node[0] == 'add_up':
            Driver.key_press('w','+')
        if node[0] == 'add_down':
            Driver.key_press('s','+')
        if node[0] == 'add_left':
            Driver.key_press('a','+')
        if node[0] == 'add_right':
            Driver.key_press('d','+')
        if node[0] == 'sub_up':
            Driver.key_press('w','-')
        if node[0] == 'sub_down':
            Driver.key_press('s','-')
        if node[0] == 'sub_left':
            Driver.key_press('a','-')
        if node[0] == 'sub_right':
            Driver.key_press('d','-')
        if node[0] == 'mult_up':
            Driver.key_press('w','*')
        if node[0] == 'mult_down':
            Driver.key_press('s','*')
        if node[0] == 'mult_left':
            Driver.key_press('a','*')
        if node[0] == 'mult_right':
            Driver.key_press('d','*')
        if node[0] == 'div_up':
            print("hello")
            Driver.key_press('w','/')
        if node[0] == 'div_down':
            print('hello2')
            Driver.key_press('s','/')
        if node[0] == 'div_left':
            print('hello3')
            Driver.key_press('a','/')
        if node[0] == 'div_right':
            print(hello4)
            Driver.key_press('d','/')
        if node[0] == 'var':
            Driver.key_press_4(node[2],node[3],node[1])
        if node[0] == 'assign':
            Driver.key_press_2(node[2],node[3],node[1])
        if node[0] == 'value':
            Driver.key_press_3(node[1],node[2])
        else:
            self.bool=False