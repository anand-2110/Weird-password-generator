import random as r
import time as t
lU="Q,W,E,R,T,Y,U,I,O,P,L,K,J,H,G,F,D,S,A,Z,X,C,V,B,N,M" 
lL='q,w,e,r,t,y,u,i,o,p,l,k,j,h,g,f,d,s,a,z,x,c,v,b,n,m'
nu=["1","2","3","4","5","6","7","8","9","0"]
ls="!,@,%,&*,( .){,}:? `,~,/' :; ,'[]= +"   
lu=lU.split(',')
limit=int(input("How many passwords do you want:- "))
f=open("PASSWOD.txt","w+")
paswdCount=0
copycount=0
copypass=[]
paswdls=[]
lx=lL.split(',')
#while paswdCount<limit:
    #if limit>1000:
    #    print(paswdCount+1)
while paswdCount<limit:
    paswd=''
    pc=0
    lowCount=0
    spCount=0
    numCount=0
    upperCount=0
    usedLow=[]
    usedUpp=[]
    usedsp=[]
    UsedNum=[]
    while (pc<16):
    
        mainnum=r.randint(1,4)

        #starting of random chars.
        if mainnum==1: #lower
            if lowCount<4:
                wr=r.choice(lx)
                if wr not in usedLow:
                    paswd+=wr
                    usedLow.append(wr)
                    lowCount+=1
                    pc+=1
                
        elif mainnum==2: #Upper
            if upperCount<4:
                wr=r.choice(lu)
                if wr not in usedUpp:
                    paswd+=wr
                    usedUpp.append(wr)
                    upperCount+=1
                    pc+=1
                
        elif mainnum==3: #number 
            if numCount<4:
                wr=r.choice(nu)
                if wr not in UsedNum:
                    paswd+=wr
                    UsedNum.append(wr)
                    numCount+=1
                    pc+=1
                    
        elif mainnum==4:#Special
            if spCount<4:
                wr=r.choice(ls)
                if wr not in usedsp:
                    paswd+=wr
                    usedsp.append(wr)
                    spCount+=1 
                    pc+=1



    #print(paswd)

    if paswd not in paswdls:
        paswdls.append(paswd)
        paswdCount+=1
        #print(paswd)
        f.write(paswd)
        f.write("\n")
print("Count of passwords so far is :", paswdCount)
#for i in paswdls:
#    print(i)
print("******************************** ********************************")
print("Count of copy passwords so far is :", copycount)
f.close()









