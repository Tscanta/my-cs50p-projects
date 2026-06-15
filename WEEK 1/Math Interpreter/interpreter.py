#MATHEMATICAL INTERPRETER

expression = input("Expression: ")#getting the expression from the user

x, y, z = expression.split() #splitting the expression into three different components x,y and z

#converting to float variables
x = float(x)
z = float(z)

#checking
if y == '+':
    answer = x + z
elif y == '-':
    answer = x - z

elif y == '/':
    answer = x / z

elif y == '*':
    answer = x * z

print(f"{answer:.1f}")


