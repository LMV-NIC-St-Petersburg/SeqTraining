import os
import subprocess
from Bio import SeqIO
import sys

#usage: python3 subtype.py reference.fasta

reference = sys.argv[1]
genes = []
for seq in SeqIO.parse(reference, 'fasta'):
	genes.append(seq.id)
samples = []

with open('sample_list.csv', 'r') as smp_list:
	for line in smp_list.readlines():
		smp = line.strip('\n')
		os.system("cat barcode"+smp+"/*.fastq.gz > "+smp+".fastq.gz") 
		samples.append(smp)
for sample in samples:
	print(sample)
	os.system("minimap2 -aY -x map-ont -t "+str(os.cpu_count())+" "+reference+" "+sample+".fastq.gz | samtools view -bS | samtools sort -o "+sample+".bam")
	os.system("samtools index "+sample+".bam")
	print(sample)
	os.system("samtools idxstats "+sample+".bam")
	os.system("samtools idxstats "+sample+".bam > "+sample+"_idxstats.txt")
	os.system("echo "+sample+" >> idxstats.txt")
	os.system("samtools idxstats "+sample+".bam >> idxstats.txt")
	os.system("samtools stats "+sample+".bam > "+sample+".bamstats")
	os.system("plot-bamstats -p "+sample+"_bamstats/ "+sample+".bamstats")
	os.system("rm "+sample+".bamstats")
	os.system("samtools depth -aa  "+sample+".bam > "+sample+"_depth.txt")
	os.system("samtools mpileup -aa -A -d 0 -Q 0 "+sample+".bam | ivar consensus -p "+sample+" -q 15 -m 5 -i "+sample)
	os.system("rm "+sample+".qual.txt")
	os.system("medaka_consensus -i "+sample+".fastq.gz -d "+sample+".fa -o medaka_"+sample)
	os.system("cp medaka_"+sample+"/consensus.fasta "+sample+"_final.fa")
	os.system("python3 plot_cov.py "+sample+"_depth.txt")
os.system("cat "+"*"+"_"+segment+"_final.fa"+" > "+segment+".fas")
