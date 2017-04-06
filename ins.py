class Interpreter:
    def __init__(self):
        self.stack=[]
        self.environment={}

    def LOAD_VALUE(self,val):
        self.stack.append(val)

    def STORE_NAME(self,name):
        val=self.stack.pop()
        self.environment[name]=val

    def LOAD_NAME(self,name):
        val=self.environment[name]
        self.stack.append(val)

    def ADD_TWO_VALUES(self):
        first=self.stack.pop()
        second=self.stack.pop()
        self.stack.append(first+second)

    def PRINT_ANSWER(self):
        print(self.stack.pop())

    def run_code(self,what_to_excute):
        instructions=what_to_excute['instructions']
        for ins in instructions:
            instruction,argument=ins
            argument=self.parse_argument(instruction,argument,what_to_excute)
            bytecode_method=getattr(self,instruction)
            if argument is None:
                bytecode_method()
            else:
                bytecode_method(argument) 
                

    def parse_argument(self,instruction,argument,what_to_excute):
        numbers=['LOAD_VALUE']
        names=['LOAD_NAME','STORE_NAME']
        if instruction in numbers:
            argument=what_to_excute['numbers'][argument]
        elif instruction in names:
            argument=what_to_excute['names'][argument]
        return argument

what_to_excute={
    "instructions": [("LOAD_VALUE", 0),
                     ("STORE_NAME", 0),
                     ("LOAD_VALUE", 1),
                     ("STORE_NAME", 1),
                     ("LOAD_NAME", 0),
                     ("LOAD_NAME", 1),
                     ("ADD_TWO_VALUES", None),
                     ("PRINT_ANSWER", None)],
    "numbers": [1, 2],
    "names":   ["a", "b"] }

instruction=Interpreter()
instruction.run_code(what_to_excute)

    
