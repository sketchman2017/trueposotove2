# -*- coding: UTF-8 -*-

a = []

with open("test04.txt") as f:
    n, m = f.readline().split(" ")
    n = int(n)
    m = int(m)

    i = 1
    while i<=n:
        s = f.readline()
        j = 1
        a.append([])
        while j<=m:            
            if s[j-1] == '.':
                a[i-1].append(0) 
            if s[j-1] == '*':
                a[i-1].append(-1)
            j+=1
        i+=1

    i1, j1, i2, j2 = f.readline().split(" ")
i1 = int(i1)
j1 = int(j1)
i2 = int(i2)
j2 = int(j2)

a[i1-1][j1-1] = 1
k = 1

while a[i2-1][j2-1] == 0:
    i = 1
    while i<=n:
        j = 1
        while j<=m:
            if a[i-1][j-1]==k:
                if i-2>=0 and a[i-2][j-1] == 0:
                    a[i-2][j-1] = k+1                 
                if j-2>=0 and a[i-1][j-2] == 0:
                    a[i-1][j-2] = k+1                 
                if i<n and a[i][j-1] == 0:
                    a[i][j-1] = k+1                 
                if j<m and a[i-1][j] == 0:
                    a[i-1][j] = k+1                 
            j+=1
        i+=1

    k+=1

with open("output.txt", "w") as f:
    f.write('%d' % a[i2-1][j2-1])
