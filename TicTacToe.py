# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 08:48:02 2020

@author: PC
"""
import copy


def Actions(s):
    actions=[] # Retourne toutes les possibilités du joueur
    for i in range(len(s)):
        for j in range(len(s)) :
            if (s[i][j]==' '):
                actions.append((i,j))
    return actions


def Resultat(s,a,joueur):
    nouvelEtat= copy.deepcopy(s) #deepcopy est utilisé afin de ne pas modifier s
    nouvelEtat[a[0]][a[1]]=joueur
    return nouvelEtat # renvoi une copie de s avec le nouveau coup joué
    
def Resultatjvj(s,a,joueur):
    s[a[0]][a[1]]=joueur
    return s    

def Terminal_Test(s):
    for i in s: #permet de vérifier si une ligne est complétée par le joueur 1 ou 2 
        joueur1 = i.count('X')
        joueur2 = i.count('O')
        if(3 in (joueur1, joueur2)):
            return True
        
    for j in range(len(s)) :  #permet de vérifier si une colonne est complétée par le joueur 1 ou 2
        joueur1=0
        joueur2=0
        for i in range(len(s)):
            if(s[i][j]=='X'):
                joueur1+=1
            elif(s[i][j]=='O'):
                joueur2+=1
        if(3 in (joueur1, joueur2)):
            return True 
        
    joueur1=[0,0] #le premier élement de la liste représente la diagonale descendante, le second la montante
    joueur2=[0,0]
    for i in range(len(s)): #permet de vérifier si une diagonale est gagnante pour un des deux joueurs
        for j in range(len(s)):
            if(i==j):  #Diagonale descendante
                if(s[i][i]=='X'):
                    joueur1[0]+=1
                elif(s[i][i]=='O'):
                    joueur2[0]+=1    
            if(i+j==2): #Diagonale montante
                if(s[i][j]=='X'):
                    joueur1[1]+=1
                elif(s[i][j]=='O'):
                    joueur2[1]+=1
    if((3 in joueur1) or (3 in joueur2)):
        return True 
    
    compteur=0 #permet de compter les cases vides (les ' ')            
    for i in range(len(s)):  #on vérifie si le tableau est complet
        for j in range(len(s)):
            if(s[i][j]==' '):
                compteur+=1
    if(compteur>0):
        return False
    else:
        return True

def Utility(s):
    for i in s: #On cherche à attribuer un score en fonction du joueur qui a complété une ligne  
        joueur1 = i.count('X')
        joueur2 = i.count('O')
        if(joueur1==3):
            return 1
        elif(joueur2==3):
            return -1
        
    for j in range(len(s)) :  #On cherche à attribuer un score en fonction du joueur qui a complété une colonne
        joueur1=0
        joueur2=0
        for i in range(len(s)):
            if(s[i][j]=='X'):
                joueur1+=1
            elif(s[i][j]=='O'):
                joueur2+=1
        if(joueur1==3):
            return 1
        elif(joueur2==3):
            return -1
        
    joueur1=[0,0] #le premier élement de la liste représente la diagonale descendante, le second la montante
    joueur2=[0,0]
    for i in range(len(s)): #On cherche à attribuer un score en fonction du joueur qui a complété une diagonale
        for j in range(len(s)):
            if(i==j):
                if(s[i][i]=='X'):
                    joueur1[0]+=1
                elif(s[i][i]=='O'):
                    joueur2[0]+=1
                
            if(i+j==2):
                if(s[i][j]=='X'):
                    joueur1[1]+=1
                elif(s[i][j]=='O'):
                    joueur2[1]+=1
    if(3 in joueur1):
        return 1
    elif(3 in joueur2):
        return -1
    
    return 0 #cas d'égalité 
    
#---------------------------- MiniMax ----------------------------------------#      
        
def MinimaxDecision(s):
    vMax=float('-inf') 
    action=(-1,-1) 
    for i in Actions(s):
        if Utility(Resultat(s,i,'X'))==1:
            return i
        elif Utility(Resultat(s,i,'O'))==-1:
            return i
        v=MaxValue(s)
        if(v>vMax):
            vMax=v
            print(vMax)
            action=i
    return action
          
def MaxValue(s):
    if(Terminal_Test(s)):
        return Utility(s)
    v=float('-inf')
    
    for i in Actions(s):
        
        v=max(v,MinValue(Resultat(s,i,'X')))
    return v

def MinValue(s):
    if(Terminal_Test(s)):
        return Utility(s)
    v=float('inf')
    for i in Actions(s):
        v=min(v,MaxValue(Resultat(s,i,'O'))) 
    return v 

#-----------------------------------------------------------------------------#
    
#-----------------------------Alpha-Beta--------------------------------------#
 
def AlphaBeta_Decision(s):
    action=(-1,-1)
    vMax=Max_Value(s,float('-inf'),float('inf'))
    for i in Actions(s):
        v=Max_Value(Resultat(s,i,'X'),float('-inf'),float('inf'))
        if(v>=vMax):
            vMax=v
            action=i
    return action

def Max_Value(s,alpha,beta):
    if(Terminal_Test(s)):
        return Utility(s)
    v=float('-inf')
    for i in Actions(s):
        v=max(v,Min_Value(Resultat(s,a,'X'),alpha,beta))
        if(v>=beta):
            return v
        alpha=max(alpha,v)
    return v

def Min_Value(s,alpha,beta):
    if(Terminal_Test(s)):
        return Utility(s)
    v=float('inf')
    for i in Actions(s):
        v=max(v,Max_Value(Resultat(s,a,'O'),alpha,beta))
        if(v<=alpha):
            return v
        beta=min(beta,v)
    return v
#-----------------------------------------------------------------------------#
            

            
def Test(): 
    
    s=[
      [1,2,1],
      [2,2,2],
      [1,1,2],
      ]

    for i in test:
        print(i)
    print('\n')
    a_liste=Actions(test)
    for i in a_liste:
        print(i)
    print('\n')
    t=Resultat(test, a_liste[0],'O')
    for i in t:
        print(i)
    print('\n')
    for i in test:
        print(i)
    print('\n')
    print(Terminal_Test(test))
    print('\n')
    print(Utility(t))

        
    

#if __name__ =='__main__' :
        
#    Test()
   
#-----------------------------------------------------------------------------#


def affiche(s):
    print("  1 2 3") #fonction d'affichage du morpion
    x=1
    for i in s:
        print(str(x)+' ',end='')
        for j in i:
            if(j==' '):
                print("_|",end="")
            if(j=='X'):
                print("X|",end="")
            if(j=='O'):
                print("O|",end="")
           
        x+=1
        print('\n')
        
        
#-----------------------------------------------------------------------------#        

def demarre ():
    print("Jeu du Morpion")
    s=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' '],]

    
    mode = input("Voulez-vous jouer au mode JvsJ, IAvsJ ou IAvsIA ? Taper 1, 2 ou 3 : ")
    while mode not in ['1','2','3']:
        print("Entrée invalide: ")
        mode = input("Voulez-vous jouer au mode JvsJ, IAvsJ ou IAvsIA ? Taper 1, 2 ou 3 : ")
    if mode=='1': # JVJ
        affiche(s) 
        x=0
        while not Terminal_Test(s):
            print("Tour du joueur "+str(x+1)+":")
            a=joue(s)
            if x==0:
                s[a[0]][a[1]]= 'X'
            else:
                s[a[0]][a[1]]= 'O'
            affiche(s)
            x=x^1
        if Utility(s)==0:
            print("Egalité")
        elif Utility(s)==-1:
            print("Victoire du joueur 2")
        else:
            print("Victoire du joueur 1")
            
    if mode =='2': # JvIA
        ans = int(input("Voulez vous jouer contre l'IA minimax ou alphabeta ? tapez 1 ou 2 : "))
        while ans not in[1,2]:
            ans = int(input("Voulez vous jouer contre l'IA minimax ou alphabeta ? tapez 1 ou 2 : "))
        if ans ==1:
           x=1
           print("Tour de l'IA: ")
           s[0][0]="X"
           affiche(s)
           while not Terminal_Test(s):
               
               if x==0:
                  
                   print("Tour de l'IA: ")
                   s= Resultat(s,MinimaxDecision(s),'X')
                   
                   affiche(s)
               else:
                   print("Tour du joueur: ")
                   
                   a = joue(s)
                   s[a[0]][a[1]]="O"
                   affiche(s)
               x=x^1
           if Utility(s)==0:
               print("Egalité")
           elif Utility(s)==-1:
               print("Victoire du joueur ")
           else:
               print("Victoire de l'IA")   
                   
               
               
#-----------------------------------------------------------------------------#            
def joue(s):
    x = int(input("Sur quelle ligne souhaitez vous jouer? "))-1        
    y = int(input("Sur quelle colonne souhaitez vous jouer? "))-1   
    while(x not in [0,1,2] and y not in [0,1,2]):
       print("Mauvaise entrée, veuillez recommencer: ")
       x = int(input("Sur quelle ligne souhaitez vous jouer? "))-1        
       y = int(input("Sur quelle colonne souhaitez vous jouer? "))-1 
    while s [x][y]!=' ':
       print("Case déjà utilisée, veuillez recommencer: ")
       x = int(input("Sur quelle ligne souhaitez vous jouer? "))-1        
       y = int(input("Sur quelle colonne souhaitez vous jouer? "))-1 
    return [x,y]
        
demarre()
