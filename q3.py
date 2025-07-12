

#for finding A^p where A is a square matrix and p is the power
def mul(mat1,mat2):
    num = len(mat1)#number of rows = columns 
    r = [[0]*num for _ in range(num)]#initially create a matrix with zeros so that we can use it for sum
    
    #we are using for loop to go over the row and columns
    for i in range(num):
        for j in range(num):
            for k in range(num):
                r[i][j] = r[i][j] + mat1[i][k]*mat2[k][j]#we are multiplying our matrix and adding with r matrix(initially with 0 values) 
                                                         
            
    return r

def matrix_power(A,p):
    #we are creatng identity matrix
    n = len(A)
    r = []#empty list
    for i in range(n):
        row = []
        for j in range(n):
            if i==j:
                row.append(1)#diagonal = 1
            else:
                row.append(0)#non diagonal = 0
        r.append(row)
    
    for _ in range(p):
        r = mul(r,A)

    return r

mat = [[1,2,3],[4,5,6],[6,7,8]]

p1 = int(input("enter the power:"))
ans = matrix_power(mat,p1)

print(ans)
