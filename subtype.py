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
	depths = ""
	for segment in genes:
		os.system("echo "+segment)
		os.system("samtools depth -aa -r "+segment+" "+sample+".bam > "+sample+"_"+segment+"_depth.txt")
		os.system("samtools mpileup -aa -A -d 0 -Q 0 -r "+segment+" "+sample+".bam | ivar consensus -p "+sample+"_"+segment+" -q 15 -m 5 -i "+sample+"_"+segment)
		depths += sample+"_"+segment+"_depth.txt "
		os.system("rm "+sample+"_"+segment+".qual.txt")
		os.system("medaka_consensus -i "+sample+".fastq.gz -d "+sample+"_"+segment+".fa -o medaka_"+sample+"_"+segment)
	os.system("python3 influenza_cov.py "+sample+"_idxstats.txt "+depths)
	os.system("cp medaka_"+sample+"_"+segment+"/consensus.fasta "+sample+"_"+segment+"_final.fa")
for segment in genes:
    os.system("cat "+"*"+"_"+segment+"_final.fa"+" > "+segment+".fas")
os.system("multiqc .")
