import re
import math
import matplotlib.pyplot as plt
import numpy as np

class Evaluate:
    def __init__(self):
        self.expression=str()



    @property
    def expression(self):
        return self._expression

    @expression.setter
    def expression(self,exp):
        self._expression=exp

    def Right(self):

        left,right = self.expression.split("=")

        if re.search(r" *sin\(",right, re.IGNORECASE):
            right = right.replace("sin", 'Q')

        if re.search(r" *cos\(", right, re.IGNORECASE):
            right = right.replace("cos", 'R')

        if re.search(r" *tan\(", right, re.IGNORECASE):
            right = right.replace("tan", 'S')
        if re.search(r"ln",right,re.IGNORECASE):
            right=right.replace('ln','T')
        if re.search(r"log",right,re.IGNORECASE):
            right=right.replace('log','U')
        return right



    def infixToPostfix(self):
        s=self.Right()

        result = []
        stack = []

        for i in range(len(s)):
            c = s[i]

            if ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9'):
                result.append(c)
            elif c == '(':
                stack.append(c)
            elif c == ')':
                while stack and stack[-1] != '(':
                    result.append(stack.pop())
                stack.pop()  # Pop '('
            else:
                while stack and (prec(s[i]) < prec(stack[-1]) or
                                (prec(s[i]) == self.prec(stack[-1]) and associativity(s[i]) == 'L')):
                    result.append(stack.pop())
                stack.append(c)

        while stack:
            result.append(stack.pop())

        exp=''.join(result)
        self.expression=exp


    def evalPostfix(self,X :float):
        postStack=[]

        exp=self.expression
        i=0

        while i <len(exp):
            if exp[i].isalpha():
                if exp[i]=='Q':
                    i=i+1
                    if exp[i].isdigit():
                        postStack.append(str(math.sin(float(exp[i]))))
                    else:
                        postStack.append(str(math.sin(float(X))))
                elif exp[i]=='R':
                    i=i+1
                    if exp[i].isdigit():
                        postStack.append(str(math.cos(float(exp[i]))))
                    else:
                        postStack.append(str(math.cos(float(X))))
                elif exp[i]=='S':
                    i=i+1
                    if exp[i].isdigit():
                        postStack.append(str(math.tan(float(exp[i]))))
                    else:
                        postStack.append(str(math.tan(float(X))))

                elif exp[i]=='T':
                    i=i+1
                    if exp[i].isdigit():
                        postStack.append(str(math.log(float(exp[i]),math.e)))
                    else:
                        postStack.append(str(math.log(float(X),math.e)))
                elif exp[i]=='U':
                    i=i+1
                    if exp[i].isdigit():
                        postStack.append(str(math.log(float(exp[i]),10)))
                    else:
                        postStack.append(str(math.log(float(X),10)))

                elif exp[i]=='e':
                    postStack.append(str(math.e))


                elif exp[i]=='x':
                    postStack.append(str(X))
            elif exp[i].isdigit():
                postStack.append(exp[i])

            else:
                var2=postStack.pop()

                var1=postStack.pop()

                if exp[i]=='+':
                    postStack.append(float(var1)+float(var2))

                elif exp[i]=='-':
                    postStack.append(float(var1)-float(var2))
                elif exp[i]=='*':
                    postStack.append(float(var1)*float(var2))
                elif exp[i]=='/':
                    postStack.append(float(var1)/float(var2))
                elif exp[i]=='^':
                    postStack.append(float(var1)**float(var2))
            i=i+1

        return_val= postStack.pop()
        return return_val


    def plotFunction(self, x_values, y_values):
        plt.plot(x_values, y_values)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Function Plot')
        plt.grid(True)
        plt.show()


def main():
    exp = Evaluate()
    exp.expression=getExpression()
    exp.expression=replaceSpace(exp.expression)
    exp.infixToPostfix()
    if 'T' in exp.expression or 'U' in exp.expression:
        x_values = np.linspace(0.00000000000001, 20, 40)  # Adjust the range as needed
        y_values = [exp.evalPostfix(x) for x in x_values]
    else:
        x_values = np.linspace(-10, 10, 35)  # Adjust the range as needed
        y_values = [exp.evalPostfix(x) for x in x_values]


    exp.plotFunction(x_values, y_values)

def getExpression():
    return(input("Enter the funciton : "))


def replaceSpace(exp):
    final_exp=exp.replace(" ","")
    return final_exp

def associativity(c):
        if c == '^':
            return 'R'
        return 'L'
def prec(c):
        if c == '^':
            return 3
        elif c == '/' or c == '*':
            return 2
        elif c == '+' or c == '-':
            return 1
        else:
            return -1

if __name__=='__main__':
    main()
