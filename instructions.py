what_to_excute={
    "instructions":[('LOAD_VALUE',0),('LOAD_VALUE',1),('ADD_TWO_VALUES',None),('PRINT_ANSWERS',None)],
    "numbers":[7,5]
    }


class Instructions:
    def __init__(self):
        self.stack=[]

    def LOAD_VALUE(self,number):
        self.stack.append(number)

    def ADD_TWO_VALUES(self):
        first=self.stack.pop()
        second=self.stack.pop()
        self.stack.append(first+second)

    def PRINT_ANSWER(self):
        print(self.stack.pop())

    def run_code(self,what_to_excute):
        instructions=what_to_excute['instructions']
        numbers=what_to_excute['numbers']

        for inst in instructions:
            instruction,argument=inst
            if instruction=='LOAD_VALUE':
                self.LOAD_VALUE(numbers[argument])
            elif instruction=='ADD_TWO_VALUES':
                self.ADD_TWO_VALUES()
            elif instruction=='PRINT_ANSWERS':
                self.PRINT_ANSWER()


instruction=Instructions()
instruction.run_code(what_to_excute)
