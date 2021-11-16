
# Import modules
# If biopython not installed then install in terminal: pip install biopython
from Bio import pairwise2
from Bio.pairwise2 import format_alignment

# Define a 2D list of our sequences
sequences = [['GATTACA','ATTACATTAC'],
             ['ATATATATAT','ATATATATATA'],
             ['AAAATAAATAAA','AATAATAATAAT'],
             ['ATATGTATACAT','ATATACACACA']]
# Define lists to store allingnments
glob = []
loc = []

#Global allignments

#Defines function to globally allign all sequences
def global_allign(seq,ref):
    # Aligns sequence using pairwise2 with allignment set to global
    alignments = pairwise2.align.globalxx(ref, seq)
    # returns a list of the best allignments
    return alignments



#Local allignments

# Defines function to locally allign all sequences
def local_allign(seq,ref):
    # Aligns sequence using pairwise2 with allignment set to local
    alignments = pairwise2.align.localxx(ref, seq)
    # returns a list of the best allignments
    return alignments

#Store list of all allignments
for pair in sequences:
    loc.append(local_allign(pair[0],pair[1]))
    glob.append(global_allign(pair[0], pair[1]))

# Output all alignments
print("All Global allignments")
for i in range(0,len(glob)):
    print("Sequences: ",sequences[i])
    for j in range(0,len(glob[i])):
        print(format_alignment(*glob[i][j]))


print("All Local allignments")
for i in range(0,len(loc)):
    print("Sequences: ",sequences[i])
    for j in range(0,len(loc[i])):
        print(format_alignment(*loc[i][j]))


