# Copy your updated FrequentWords function (along with all required subroutines) below this line

# Input:  A string Text and an integer k
# Output: A list containing all most frequent k-mers in Text
def FrequentWords(Text, k):
    FrequentPatterns = []
    Count = CountDict(Text, k)
    m = max(Count.values())
    for i in Count:
        if Count[i] == m:
            FrequentPatterns.append(Text[i:i+k])
    FrequentPatternsNoDuplicates = remove_duplicates(FrequentPatterns)
    return FrequentPatternsNoDuplicates

# Input:  A list Items
# Output: A list containing all objects from Items without duplicates
def remove_duplicates(Items):
    ItemsNoDuplicates = [] # output variable
	#Remove all duplicates
    newSequence = list(Items)
    for element in newSequence:
        duplicates = newSequence.count(element) - 1
        if duplicates >= 1:
            for i in range(duplicates):
                newSequence.remove(element)
    return newSequence

# Input:  A string Text and an integer k
# Output: CountDict(Text, k)
def CountDict(Text, k):
    Count = {} # output variable
    # fill in the rest of the CountDict function here.
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        Count[i] = PatternCount(Pattern, Text)
    return Count

# Input:  Strings Pattern and Text
# Output: The number of times Pattern appears in Genome
def PatternCount(Pattern, Genome):
    count = 0 # output variable
    for i in range(len(Genome)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count

# Input:  String Pattern
# Output: String Pattern without duplicates
def remove_duplicates(Pattern):
    newSequence = list(Pattern)
    for element in newSequence:
        duplicates = newSequence.count(element) - 1
        if duplicates >= 1:
            for i in range(duplicates):
                newSequence.remove(element)
    return newSequence

def reversed_string(a_string):
    return a_string[::-1]
    
def ReverseComplement(dna, reverse):
    bases = 'ATGCTACG'
    complement_dict = {bases[i]:bases[i+4] for i in range(4)}
    if reverse:
        dna = reversed(dna)
    result = [complement_dict[base] for base in dna]
    return ''.join(result)

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

Pattern = raw_input("Pattern: ")

#Convert to string
result=str(PatternMatching(Pattern,Genome))
#Remove [] and remove '
print result.strip('[]').replace(",","")