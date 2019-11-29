import random
import threading
Nucleotides=['A','T','C','G']

codonDict = { 
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                  
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L', 
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W', 
    } 

def randomCodon():
    return ''.join([random.choice(Nucleotides) for i in range(3)])

def randomDNASequence(n):
    return ''.join([randomCodon() for i in range(n)])

class dnaTranslate(threading.Thread):
    def __init__(self,dnaSequence):
        threading.Thread.__init__(self)
        self.dnaSequence=dnaSequence
        self.proteinSequence=[]
    def run(self):
        nOfCodon=len(self.dnaSequence)//3
        activeProtein=''
        for i in range(nOfCodon):
            codonStart=3*i
            codonEnd=codonStart+3
            codon=self.dnaSequence[codonStart:codonEnd]
            translation=codonDict.get(codon)
            if translation!='_':
                activeProtein+=translation
            else:
                self.proteinSequence.append(activeProtein)
                activeProtein=''
        if (activeProtein!=''):
            self.proteinSequence.append(activeProtein)


if __name__ == "__main__":
    sequence=randomDNASequence(80)
    print(sequence)
    t=dnaTranslate(sequence)
    t.start()
    t.join()
    print(t.proteinSequence)
