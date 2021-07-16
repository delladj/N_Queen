import cython
import numpy as np
import time
# Verification de la solution
def Verif(rns, lign, col):
            for i in range(len(rns)) :
                if rns[i] == col or lign - i == abs(rns[i] - col):
                    return False
            return True

# Création de la matrice qui représente l'échuiquier
def Echiq (n,rns) :
    m=np.zeros([n,n])
    for i in range (n) :
        m[i][rns[i]]=1
    return m

# Largeur d'abord
def N_Reines_Larg(n) :
        file = []
        for i in range(n):
            file += [[i]]          
        while file :
            rns = file.pop()
            if len(rns)==n :
                return Echiq(n,rns)
            for i in range(n):
                if Verif(rns,len(rns),i):
                    file.insert(0, rns + [i])
        return False
   
# Profondeur d'abord
def Prof(n, lign, clns, rns):
            if rns :
                return
            if lign == n:
                rns.append(clns)
                return
            for i in range(n):
                if Verif(clns, lign, i ):
                    Prof(n, lign + 1, clns + [i], rns)
def N_Reines_Prof(n) :
        rns = []
        Prof(n, 0, [], rns)
        if rns : return Echiq(n,rns[0])
        return False

# Algorithme A*

def Heurist(n,i):
    G_n = i
    H_n = n - i
    F_n = G_n + H_n
    return F_n

def A_Star(n) :
        opn = []
        for i in range(n):
            opn += [[i]]          
        while opn :
            clos = opn.pop()
            for i in range(n):
                if Heurist(n,i) <= Heurist(n,i-1) and Verif(clos,len(clos),i) :
                    opn.insert(0, clos + [i])
            if len(clos)==n :
                return Echiq(n,clos)
        return False

N = [26]
Tmp_Prof = [0]*len(N)


start = time.time()
N_Reines_Prof(N[0])
Tmp_Prof[0]= time.time()-start
print(Tmp_Prof)




