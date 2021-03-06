import random
import threading
import requests
import json
import time
from multiprocessing import Process
Nucleotides = ['A', 'T', 'C', 'G']
# humanGenomeURL = 'https://api.genome.ucsc.edu/list/chromosomes?genome=hg38'
# humanGenome = requests.get(humanGenomeURL).json()
# chromosomeList = list(humanGenome['chromosomes'].keys())
chromosomeBaseURL = 'https://api.genome.ucsc.edu/getData/sequence?genome=hg38;chrom='
availableChromosome = []
availableChromosome=json.load(open('chromosomes.json'))['chromosomes'][:20]


codonDict = {
    'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
    'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
    'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
    'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
    'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
    'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
    'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
    'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
    'TAC': 'Y', 'TAT': 'Y', 'TAA': 'STOP', 'TAG': 'STOP',
    'TGC': 'C', 'TGT': 'C', 'TGA': 'STOP', 'TGG': 'W',
}


def translate(chromo):
    dnaSequenceDict = requests.get(chromosomeBaseURL+chromo).json()
    dnaSequence = dnaSequenceDict['dna'].upper()
    proteinSequence = []
    nOfCodon = len(dnaSequence)//3
    activeProtein = ''
    for i in range(nOfCodon):
        codonStart = 3*i
        codonEnd = codonStart+3
        codon = dnaSequence[codonStart:codonEnd]
        translation = codonDict.get(codon)
        if translation != 'STOP':
            activeProtein += translation
        else:
            proteinSequence.append(activeProtein)
            activeProtein = ''
    if (activeProtein != ''):
        proteinSequence.append(activeProtein)
    return proteinSequence


class dnaTranslate(threading.Thread):
    def __init__(self, chromo):
        threading.Thread.__init__(self)
        self.chromo = chromo
        self.proteinSequence = []

    def run(self):
        self.proteinSequence = translate(self.chromo)

def main():
    print(f"Using {len(availableChromosome)} chromosomes")
    # MultiThread
    Threads = []
    for chromo in availableChromosome:
        Threads.append(dnaTranslate(chromo))
    tic = time.time()
    for t in Threads:
        t.start()
    for t in Threads:
        t.join()

    toc = time.time()
    print(f"Multithread execution time : {toc-tic}")

    # For-loop

    tic=time.time()
    for chromo in availableChromosome:
        translate(chromo)
    toc=time.time()
    print(f"For-loop execution time : {toc-tic}")

    # Multiprocess
    ## YOU CAN UNCOMMENT THIS PART TO CHECK THE PERFORMANCE BUT
    ## THIS IS NOT PART OF THE COURSE
    # processes = []
    # for chromo in availableChromosome:
    #     p = Process(target=translate, args=(chromo,))
    #     processes.append(p)
    # tic = time.time()
    # for p in processes:
    #     p.start()
    # for p in processes:
    #     p.join()
    # toc = time.time()
    # print(f"Multiprocessing execution time : {toc-tic}")


if __name__ == "__main__":
    main()
    
