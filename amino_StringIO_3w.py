import pandas as pd
import numpy as np
import sys
import io

X=pd.read_csv("/Users/inouemasafumi/OneDrive/python3/aminomap/Uniplot/Human20413.txt",sep="\t")
print(X.head())


Seq=X["Sequence"]
Seqlist=Seq.values.tolist()
WPS=(str(Seqlist).replace("," , "")) #replace, deletion comma, the sequence data joined, and each seq separated with space.

file = open("/Users/inouemasafumi//OneDrive/python3/aminomap/Uniplot/result/WPS_Human20413.txt","w")
file.write(WPS)
file.close()


with io.StringIO() as f:
    sys.stdout = f # the output into f
    X1 = ["A","G","S","T","V","L","I","F","Y","W","H","Q","N","E","D","K","R","P","C","M"]
    #output=[]
    for N1 in (X1):
        for N2 in (X1): # in 16,17; tab is needed to order below
            for N3 in (X1):
                #for N4 in (X1):
                    #for N5 in (X1):
                        Nc="".join([N1,N2,N3])
                        Xc=WPS.count(Nc) # count(Nc) is calculated the match number with whole-protein sequence
                        print(Nc,Xc) #the output of this commmand is necessary
    text = f.getvalue() # the output on print() is stored, inputs on text
    sys.stdout = sys.__stdout__ # the output into standard
print("STRAT/n" + text) #check the data
#print(N3,Xc)
#AA 1157253
#AG 1115451
#AS 524456
#GA 1069591
#GG 1083653
#GS 594663
#SA 497176
#SG 603048

# write code
file = open("/Users/inouemasafumi/OneDrive/python3/aminomap/Uniplot/result/Human20413_r3.txt","w")
file.write(text)
file.close()

# read code
#f=open("/Users/inouemasafumi/Documents/python3/aa_word/result/data00.txt")
#data00=f.read()
#f.close()
#print (data00)
