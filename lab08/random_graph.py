import random
import numpy as np
import scipy.stats as ss

x = random.sample(range(0,501),100)
print x

y = random.sample(range(0,501),100)
print y

#The following code tests the random sampling tested

print 'HO = there is no statistical significance'
print 'HA = there is a  statistical significance'
ttest_sampx = ss.ttest_1samp(x,250)
print ttest_sampx

#We accept the null hypothesis

print 'HO is accepted.There is no statistical significance'

ss.linregress(range(500),range(500))
print ss.linregress