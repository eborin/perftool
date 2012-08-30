# this a module with statistics functions

import math
import re
import sys

def sum(x):
	s=0
        for n in x:
                s+=n
        return s

def sqsum(x):
	s2=0
#	print 'x:', x
	for n in x:
#		print "n:", n
		s2+=pow(float(n),2.0)
#		print "s2:", s2
#	print s2
	return s2

def prod(x):
	p=1
        for val in x:
                p *= val
#		print "=====",p
#	print "----------------->",p
	return p	

def nroot(val, n):
	return float(pow(val, 1/float(n)))
	
def average(ssum, ssize):
	return float(ssum)/float(ssize)

def gmean(x):
	n=len(x)
	y=[]
#	print n
	for val in x:
		y.append(nroot(val, n))
#		print x[i]
	return prod(y)

def var(sum1, sum2, size):
#	print "sum:", sum1
#	print "sqsum:",sum2
#	print "len:",size
	try:
		v = (sum2-(pow(sum1,2)/float(size)))/float(size-1)
	except ZeroDivisionError:
		print "WARNING: something went wrong while calculating standard deviation"
		return 'error' 
	if v < 0:
		print "WARNING: something went wrong while calculating standard deviation"
                return 'error'
	return v

def stdv1(variance):
#	print variance
	return math.sqrt(variance)
		

def stdv2(sum1, sum2, size):
	return math.sqrt(var(sum1, sum2, size))

def conf(cl, stdev, df):

	if df < 0:
		print "WARNING: sample size must be at least 2"
		return 'none'

	students_t_table = [['df/p', 20, 50, 80, 90, 95, 98, 99, 99.9], [1, 0.324920, 1, 3.077684, 6.313752, 12.70620, 31.82052, 63.65674, 636.6192], [2, 0.288675, 0.816497, 1.885618, 2.919986, 4.30265, 6.96456, 9.92484, 31.5991], [3, 0.276671, 0.764892, 1.637744, 2.353363, 3.18245, 4.54070, 5.84091, 12.9240], [4, 0.270722, 0.740697, 1.533206, 2.131847, 2.77645, 3.74695, 4.60409, 8.6103], [5, 0.267181, 0.726687, 1.475884, 2.015048, 2.57058, 3.36493, 4.03214, 6.8688], [6, 0.264835, 0.717558, 1.439756, 1.943180, 2.44691, 3.14267, 3.70743, 5.9588], [7, 0.263167, 0.711142, 1.414924, 1.894579, 2.36462, 2.99795, 3.49948, 5.4079], [8, 0.261921, 0.706387, 1.396815, 1.859548, 2.30600, 2.89646, 3.35539, 5.0413], [9, 0.260955, 0.702722, 1.383029, 1.833113, 2.26216, 2.82144, 3.24984, 4.7809], [10, 0.260185, 0.699812, 1.372184, 1.812461, 2.22814, 2.76377, 3.16927, 4.5869], [11, 0.259556, 0.697445, 1.363430, 1.795885, 2.20099, 2.71808, 3.10581, 4.4370], [12, 0.259033, 0.695483, 1.356217, 1.782288, 2.17881, 2.68100, 3.05454, 4.3178], [13, 0.258591, 0.693829, 1.350171, 1.770933, 2.16037, 2.65031, 3.01228, 4.2208], [14, 0.258213, 0.692417, 1.345030, 1.761310, 2.14479, 2.62449, 2.97684, 4.1405], [15, 0.257885, 0.691197, 1.340606, 1.753050, 2.13145, 2.60248, 2.94671, 4.0728], [16, 0.257599, 0.690132, 1.336757, 1.745884, 2.11991, 2.58349, 2.92078, 4.0150], [17, 0.257347, 0.689195, 1.333379, 1.739607, 2.10982, 2.56693, 2.89823, 3.9651], [18, 0.257123, 0.688364, 1.330391, 1.734064, 2.10092, 2.55238, 2.87844, 3.9216], [19, 0.256923, 0.687621, 1.327728, 1.729133, 2.09302, 2.53948, 2.86093, 3.8834], [20, 0.256743, 0.686954, 1.325341, 1.724718, 2.08596, 2.52798, 2.84534, 3.8495], [21, 0.256580, 0.686352, 1.323188, 1.720743, 2.07961, 2.51765, 2.83136, 3.8193],[22, 0.256432, 0.685805, 1.321237, 1.717144, 2.07387, 2.50832, 2.81876, 3.7921], [23, 0.256297, 0.685306, 1.319460, 1.713872, 2.06866, 2.49987, 2.80734, 3.7676], [24, 0.256173, 0.684850, 1.317836, 1.710882, 2.06390, 2.49216, 2.79694, 3.7454], [25, 0.256060, 0.684430, 1.316345, 1.708141, 2.05954, 2.48511, 2.78744, 3.7251], [26, 0.255955, 0.684043, 1.314972, 1.705618, 2.05553, 2.47863, 2.77871, 3.7066], [27, 0.255858, 0.683685, 1.313703, 1.703288, 2.05183, 2.47266, 2.77068, 3.6896], [28, 0.255768, 0.683353, 1.312527, 1.701131, 2.04841, 2.46714, 2.76326, 3.6739], [29, 0.255684, 0.683044, 1.311434, 1.699127, 2.04523, 2.46202, 2.75639, 3.6594], [30, 0.255605, 0.682756, 1.310415, 1.697261, 2.04227, 2.45726, 2.75000, 3.6460], ['inf', 0.253347, 0.674490, 1.281552, 1.644854, 1.95996, 2.32635, 2.57583, 3.2905]]

	col=1
	while col < len(students_t_table[0]):
		if students_t_table[0][col] == cl: break
		col+=1
	if col == len(students_t_table[0]):
		print "WARNING: confidence level not supported"
		return 'none' 

	if df <= 30:
		lin = 1
		while lin < len(students_t_table):
			if students_t_table[lin][0] == df:
				tstar = students_t_table[lin][col]
				break
			lin+=1
		if lin == len(students_t_table):
			print "WARNING: could not find t critical value"
			return 'none'
	else:
		tstar = students_t_table[31][col] 
#	print 'col ', col, 'lin ', lin, 'tstar ', tstar
	return tstar*(float(stdev)/float(math.sqrt(df+1)))

def ratio(val1 , val2):
	if val == 0:
		return 0
	return float(val1)/float(val2)

def diff(val1, val2):
	return val1-val2
