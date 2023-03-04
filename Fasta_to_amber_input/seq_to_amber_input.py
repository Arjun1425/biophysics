# This code will convert a one-letter amino acid sequence to an amber_input.in file. After using this code, you will get amber_input.in file. You can use this file to generate a pdb file using tleap {tleap -f amber_input.in}. Which will generate a file called parambuilder_input.pdb. You can use this file for lammps input file. 

fasta_seq = input('Enter your pdb sequence in FASTA format: ')
amino_acids = {'A' : 'ALA', 'R' : 'ARG', 'N' : 'ASN', 'D' : 'ASP', 'C' : 'CYS', 'Q' : 'GLN', 'E' : 'GLU', 'G' : 'GLY', 'H' : 'HIS', 'I' : 'ILE', 'L' : 'LEU', 'K' : 'LYS', 'M' : 'MET', 'F' : 'PHE', 'P' : 'PRO', 'S' : 'SER', 'T' : 'THR', 'W' : 'TRP', 'Y' : 'TYR', 'V' : 'VAL', 'O' : 'PYL', 'U' : 'SEC'}

# Convert the sequence from one-letter to three-letter amino acid codes
lst = [amino_acids[i] for i in fasta_seq if i in amino_acids]

setup_IDP = ' '.join(lst)

# Write the converted sequence to an amber_input.in file
with open('amber_input.in', 'w') as f:
      f.write('\n')
      f.write('source leaprc.protein.ff14SB\n')
      f.write('\n')
      f.write(f'prot = sequence {{ {setup_IDP} }}\n')
      f.write('\n')
      f.write('savepdb prot parambuilder_input.pdb\n')
      f.write('\n')
      f.write('quit')








#sba = [*fasta_seq]
#swa = ['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V','O','U']
#lst = []
#for i in sba:
#    for j in swa:
#        if i == j:
#            lst.append(amino_acids[j])
#setup_IDP = (', '.join(lst))
#setup_IDP = setup_IDP.replace(',','')
#print(setup_IDP)
