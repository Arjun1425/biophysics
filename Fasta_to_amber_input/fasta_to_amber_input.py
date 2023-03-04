# This code will read a FASTA file (only second line) and convert a one-letter amino acid sequence to an amber_input.in file (remember the FASTA file should be in the same directory as this file). After using this code, you will get amber_input.in file. You can use this file to generate a pdb file using tleap {tleap -f amber_input.in}. Which will generate a file called parambuilder_input.pdb. You can use this file for lammps input file.

# Define the dictionary of one-letter to three-letter amino acid codes
aa_dict = {'A': 'ALA', 'R': 'ARG', 'N': 'ASN', 'D': 'ASP', 'C': 'CYS','Q': 'GLN', 'E': 'GLU', 'G': 'GLY', 'H': 'HIS', 'I': 'ILE', 'L': 'LEU', 'K': 'LYS', 'M': 'MET', 'F': 'PHE', 'P': 'PRO', 'S': 'SER', 'T': 'THR', 'W': 'TRP', 'Y': 'TYR', 'V': 'VAL', 'O' :'PYL', 'U' : 'SEC'}


# Prompt the user for the FASTA file name
filename = input("Enter the name of the FASTA file: ")

# Read in the contents of the input file
with open(filename, 'r') as f:
    # Read the second line of the file, which contains the protein sequence
    for i, line in enumerate(f):
        if i == 1:
            sequence = line.strip()
            break


# Convert the sequence from one-letter to three-letter amino acid codes
sequence_3letter = ''
for aa in sequence:
        if aa in aa_dict:
            sequence_3letter += aa_dict[aa] + ' '
        else:
            sequence_3letter += aa + ' '

# Write the converted sequence to an amber_input.in file
with open('amber_input.in', 'w') as f:
    f.write('\n')
    f.write('source leaprc.protein.ff14SB\n')
    f.write('\n')
    f.write(f'prot = sequence {{ {sequence_3letter.strip()} }}\n')
    f.write('\n')
    f.write('savepdb prot parambuilder_input.pdb\n')
    f.write('\n')
    f.write('quit')
