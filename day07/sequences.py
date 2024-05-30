
# pip install Bio

from Bio.Seq import Seq

my_dna = Seq("AGTACACTGGTAGGCCTTACAG_T")

print(my_dna)                       # AGTACACTGGTAGGCCTTACAG_T
print(my_dna.complement())          # TCATGTGACCATCCGGAATGTC_A
print(my_dna.reverse_complement())  # A_CTGTAAGGCCTACCAGTGTACT
print(my_dna.transcribe())          # AGUACACUGGUAGGCCUUACAG_U
