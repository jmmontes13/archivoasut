
from modeller import *

env = environ()
aln = alignment(env)
mdl = model(env, file='4eam.pdb', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='4EAM', atom_files='4eam.pdb')
aln.append(file='Node18.fasta', align_codes='Node', alignment_format='FASTA')
aln.align2d()
aln.write(file='aligned2.fasta', alignment_format='FASTA')
aln.write(file='aligned2.ali', alignment_format='PIR')
aln.write(file='aligned2.pap', alignment_format='PAP')
