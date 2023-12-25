sp = open('solve_problem.txt','x')
sp2 = open('solve_problem.txt','w')
a = 10
b = 20
c = a+b
sp2.write(str(c))
sp2.close()
sp2 = open('solve_problem.txt','r')
print(sp2.read())
sp2.close()