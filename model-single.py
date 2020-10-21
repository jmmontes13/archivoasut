from modeller import *
from modeller.automodel import *
#from modeller import soap_protein_od

env = environ()
a = automodel(env, alnfile='aligned.ali',
              knowns='4EAM', sequence='target',
              assess_methods=(assess.DOPE,
                              #soap_protein_od.Scorer(),
                              assess.GA341))
a.starting_model = 1
a.ending_model = 65
a.make()

# Get a list of all successfully built models from a.outputs
ok_models = filter(lambda x: x['failure'] is None, a.outputs)

# Rank the models by DOPE score
key = 'DOPE score'
ok_models.sort(lambda a,b: cmp(a[key], b[key]))

# Get top models
m = ok_models[0]
print "Top model: %s (DOPE score %.3f)" % (m['name'], m[key])
m2 = ok_models[1]
print "Top model: %s (DOPE score %.3f)" % (m2['name'], m2[key])
m3 = ok_models[2]
print "Top model: %s (DOPE score %.3f)" % (m3['name'], m3[key])
m4 = ok_models[3]
print "Top model: %s (DOPE score %.3f)" % (m4['name'], m4[key])
m5 = ok_models[4]
print "Top model: %s (DOPE score %.3f)" % (m5['name'], m5[key])
