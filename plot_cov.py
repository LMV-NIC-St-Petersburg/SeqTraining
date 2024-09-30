import sys
from matplotlib import pyplot as plt
import statistics

pos = []
cov = []
zeros = 0
lten = 0
with open(sys.argv[1], 'r') as inf:
	for line in inf:
		s = line.split()
		pos.append(int(s[1]))
		cov.append(int(s[2]))
		if int(s[2]) == 0:
			zeros += 1
		if int(s[2]) < 10:
			lten += 1
		#m = m + int(s[2])
	#m = m/pos[end]
	plt.semilogy(pos, cov)
	plt.title(str(statistics.median(cov)))
	plt.savefig(sys.argv[1].split(".")[0]+'.png')
	print("Median coverage: "+str(statistics.median(cov)))
	print("Zero-covered positions: "+str(zeros))
	print("Coverage lower than 10: "+str(lten))
		