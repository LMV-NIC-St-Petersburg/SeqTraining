import os
import subprocess

samples = []
with open('sample_list.csv', 'r') as smp_list:
	for line in smp_list.readlines():
		smp = line.strip('\n')
		os.system("cat barcode"+smp+"/*.fastq.gz > "+smp+".fastq.gz") 
		samples.append(smp)
for sample in samples:
	print(sample)
	os.system("minimap2 -aY -x map-ont -t "+str(os.cpu_count())+" all.fasta "+smp+".fastq.gz | samtools view -b | samtools sort -o "+sample+".bam")
	os.system("samtools index "+sample+".bam")
	print(sample)
	os.system("samtools idxstats "+sample+".bam")
	os.system("samtools idxstats "+sample+".bam > "+sample+"_idxstats.txt")
	os.system("echo "+sample+" >> idxstats.txt")
	os.system("samtools idxstats "+sample+".bam >> idxstats.txt")
