# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 15:59:13 2019

@author: Yujin Yoshimura
CMPS 4553 Survey Computational Methods
Dr. Tina Johnson
Program 5

This program searches through a DNA sequence to find all Open Reading Frames
(ORFs), which are sequences of amino acids that specify possible genes.
The start codon, ATG encodes for the amino acid Methionine (Met).
The stop codon will be TAA, TAG, or TGA.
Codons are groups of 3 nucleotides which code for an amino acid. Searches must
start with ATG and then look at groups of 3 searching for one of the 3 stops.
This program only looks for genes which have a nucleotide length of 1,000 or
more, because shorter sequences are not likely genes.
Since DNA is made of two strands, it is necessary to search for ORFs in the
reverse-complement DNA strand as well. Nucleotide information in the Genbank
file is only for one strand of the DNA.
"""

import re

"""
header
@param: file
@return: void
Writes header into the output file.
"""
def header(outf):
    name = 'Yujin Yoshimura'
    course = 'CMPS 4553 Survey Computational Methods'
    instructor = 'Dr. Tina Johnson'
    iteration = 'Program 5'
    description = 'This program searches through a DNA sequence to find all Open Reading Frames\n'
    description += '(ORFs), which are sequences of amino acids that specify possible genes.\n'
    description += 'The start codon, ATG encodes for the amino acid Methionine (Met).\n'
    description += 'The stop codon will be TAA, TAG, or TGA.\n'
    description += 'Codons are groups of 3 nucleotides which code for an amino acid. Searches must\n'
    description += 'start with ATG and then look at groups of 3 searching for one of the 3 stops.\n'
    description += 'This program only looks for genes which have a nucleotide length of 1,000 or\n'
    description += 'more, because shorter sequences are not likely genes.\n'
    description += 'Since DNA is made of two strands, it is necessary to search for ORFs in the\n'
    description += 'reverse-complement DNA strand as well. Nucleotide information in the Genbank\n'
    description += 'file is only for one strand of the DNA.\n'
    
    outf.write(name + '\n')
    outf.write(course + '\n')
    outf.write(instructor + '\n')
    outf.write(iteration + '\n')
    outf.write('\n')
    outf.write(description + '\n')
    outf.write('\n')

"""
compliment
@param: string
@return: string
Gives reverse compliment of a given DNA sequence.
"""
def compliment(dna):
    c = ''
    dna_dict = {
        'a': 't', #Thymine
        'g': 'c', #Cytosine
        't': 'a', #Adenine
        'c': 'g'  #Guanine
        }
    for i in range(len(dna)):
        c += dna_dict.get(dna[-i], '-')
    return c

"""
codon
@param: string
@return: list
Gives set of codons of a given DNA sequence.
"""
def codon(dna):
    c = []
    for i in range(0, len(dna), 3):
        if len(dna[i:i+3]) == 3:
            c.append(dna[i:i+3])
    return c

"""
amino_acid
@param: list
@return: string
Gives set of amino acids of a given codon sequence.
"""
def amino_acid(codon):
    a = ''
    codon_dict = {
        'ttt': 'F', #phe: Phenylalanine
        'ttc': 'F',
        'tta': 'L', #leu: Leucine
        'ttg': 'L',
        'ctt': 'L',
        'ctc': 'L',
        'cta': 'L',
        'ctg': 'L',
        'att': 'I', #ile: Isoleucine
        'atc': 'I',
        'ata': 'I',
        'atg': 'M', #met: Methionine, start codon
        'gtt': 'V', #val: Valine
        'gtc': 'V',
        'gta': 'V',
        'gtg': 'V',
        'tct': 'S', #ser: Serine
        'tcc': 'S',
        'tca': 'S',
        'tcg': 'S',
        'cct': 'P', #pro: Proline
        'ccc': 'P',
        'cca': 'P',
        'ccg': 'P',
        'act': 'T', #thr: Threonine
        'acc': 'T',
        'aca': 'T',
        'acg': 'T',
        'gct': 'A', #ala: Alanine
        'gcc': 'A',
        'gca': 'A',
        'gcg': 'A',
        'tat': 'Y', #tyr: Tyrosine
        'tac': 'Y',
        'taa': 'Z', #stop codon
        'tag': 'Z', #stop codon
        'cat': 'H', #his: Histidine
        'cac': 'H',
        'caa': 'Q', #gln: Glutamine
        'cag': 'Q',
        'aat': 'N', #asn: Asparagine
        'aac': 'N',
        'aaa': 'K', #lys: Lysine
        'aag': 'K',
        'gat': 'D', #asp: Aspartic Acid
        'gac': 'D',
        'gaa': 'E', #glu: Glutamic Acid
        'gag': 'E',
        'tgt': 'C', #cys: Cysteine
        'tgc': 'C',
        'tga': 'Z', #stop codon
        'tgg': 'W', #trp: Tryptophan
        'cgt': 'R', #arg: Arginine
        'cgc': 'R',
        'cga': 'R',
        'cgg': 'R',
        'agt': 'S', #ser: Serine
        'agc': 'S',
        'aga': 'R', #arg: Arginine
        'agg': 'R',
        'ggt': 'G', #gly: Glycine
        'ggc': 'G',
        'gga': 'G',
        'ggg': 'G'
        }
    for i in range(len(codon)):
        a += codon_dict.get(codon[i], '-')
    return a

"""
gene
@param: string, list, int
@return: void
Gives set of genes of a given amino acid sequence.
"""
def orf(amino_acid, genes, offset):
    is_gene = False
    gene = ''
    for i in range(len(amino_acid)):
        if amino_acid[i] == 'M':
            is_gene = True
            start = offset + i * 3
        if amino_acid[i] == 'Z':
            is_gene = False
            finish = offset + i * 3
            #ORFs of length less than 333 are not likely genes.
            if len(gene) > 333:
                gene = str(start) + ' - ' + str(finish) + ':\n' + gene
                genes.append(gene)
            gene = ''
        if is_gene:
            gene += amino_acid[i]

"""
main
@param: void
@return: void
Main function.
"""
def main():
    is_base = False
    dna1 = ''
    genes = []
    with open("mycoplasma.gb", "r", encoding = "utf8") as inf, open("mycoplasma.txt", "w", encoding = "utf8") as outf:
        header(outf)
        for line in inf:
            if len(re.findall('^ORIGIN', line)) > 0:
                is_base = True
            if is_base:
                dna1 += ''.join(re.findall('[atcg]', line))
        dna2 = compliment(dna1)
        orf(amino_acid(codon(dna1)), genes, 0)
        orf(amino_acid(codon(dna2)), genes, 0)
        orf(amino_acid(codon(dna1[1:])), genes, 1)
        orf(amino_acid(codon(dna2[1:])), genes, 1)
        orf(amino_acid(codon(dna1[2:])), genes, 2)
        orf(amino_acid(codon(dna2[2:])), genes, 2)
        outf.write(str(len(genes)) + ' matches found. \n\n')
        for g in genes:
            outf.write(g + '\n')

if __name__ == '__main__':
    main()