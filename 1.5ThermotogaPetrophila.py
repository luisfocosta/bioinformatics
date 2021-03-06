# Input:  Two strings, Pattern and Genome
# Output: A list containing all starting positions where Pattern appears as a substring of Genome
def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    count = 0 # output variable
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern:
            positions.append(i)
            count = count+1
    return positions

### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys

genome='AACTCTATACCTCCTTTTTGTCGAATTTGTGTGATTTATAGAGAAAATCTTATTAACTGAAACTAAAATGGTAGGTTTGGTGGTAGGTTTTGTGTACATTTTGTAGTATCTGATTTTTAATTACATACCGTATATTGTATTAAATTGACGAACAATTGCATGGAATTGAATATATGCAAAACAAACCTACCACCAAACTCTGTATTGACCATTTTAGGACAACTTCAGGGTGGTAGGTTTCTGAAGCTCTCATCAATAGACTATTTTAGTCTTTACAAACAATATTACCGTTCAGATTCAAGATTCTACAACGCTGTTTTAATGGGCGTTGCAGAAAACTTACCACCTAAAATCCAGTATCCAAGCCGATTTCAGAGAAACCTACCACTTACCTACCACTTACCTACCACCCGGGTGGTAAGTTGCAGACATTATTAAAAACCTCATCAGAAGCTTGTTCAAAAATTTCAATACTCGAAACCTACCACCTGCGTCCCCTATTATTTACTACTACTAATAATAGCAGTATAATTGATCTGA'

pattern = 'CTTGATCAT'
positions = PatternMatching(pattern, genome)
print ('Pattern: '+pattern+' appears '+str(len(positions))+' times in the Thermotoga petrophila virus genome at these positions:'),
print (positions)
pattern = 'ATGATCAAG'
positions = PatternMatching(pattern, genome)
print ('Pattern: '+pattern+' appears '+str(len(positions))+' times in the Thermotoga petrophila virus genome at these positions:'),
print (positions)