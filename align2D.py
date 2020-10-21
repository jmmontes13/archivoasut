from modeller import *
log.verbose()
env = environ()
env.io.atom_files_directory = ['./']
aln = alignment(env)
mdl = model(env)
# Read the whole 4eam atom file
mdl.read(file='4eam.pdb', model_segment=('FIRST:@', 'END:'))

aln.append_model(mdl, align_codes='4eam', atom_files="4eam.pdb")
aln.append(file='target.fasta', align_codes='target', alignment_format='FASTA')
aln.align2d()
aln.write(file='align.ali', alignment_format='PIR')
aln.write(file='align.pap', alignment_format='PAP')
