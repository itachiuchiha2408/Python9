file=open("generate_table.txt",'w')
def GenerateTable(Num):
    i=0
    k=1
    while k<=10:
        print(Num,"*",k,"=",Num*k)
        file.write(str(Num))
        file.write('*')
        file.write(str(k))
        file.write('=')
        file.write(str(Num*k))
        file.write('\n')
        k=k+1
Table=int(input("Enter a number: "))
file.write("Enter a number: ")
file.write(str(Table))
file.write('\n')
GenerateTable(Table) 