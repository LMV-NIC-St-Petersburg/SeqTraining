# SeqTraining

Устновка менеджера терминалов

Mobaxterm
https://mobaxterm.mobatek.net/download.html

Открыть Tools --> Command Prompt
Ввести:

wsl --update
wsl --install -d Ubuntu-22.04
wsl --set-version Ubuntu-22.04 1

Установка Docker Desktop

Docker Desktop
https://www.docker.com/

Установка EPI2ME Labs

EPI2ME Labs
https://labs.epi2me.io/downloads/

Установка программы Ugene (для работы с выравниваниями и визуализации сборок)

Ugene
http://ugene.net/


Установка пакета MIRA для сборки данных секвенирования вирусов SARS-CoV-2 и гриппа

Настройка MIRA в Docker
https://cdcgov.github.io/MIRA/articles/mira-dd-getting-started.html

Настойка Windows Subsystem for Linux (wsl) и установка дополнительных пакетов

Внутри wsl:

sudo apt update
sudo apt upgrade
sudo apt install tmux mc htop git nano make gcc zlib1g-dev autoconf libbz2-dev liblzma-dev libncurses5-dev g++ ttf-mscorefonts-installer ant openjdk-21-jdk

curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh 
sh Miniconda3-latest-Linux-x86_64.sh 
conda config --add channels defaults
conda config --add channels bioconda
conda config --add channels conda-forge
conda –set channel_priority strict
conda update --all
conda create -n nanopore python=3.10 fastqc multiqc fastp minimap2 samtools ivar biopython numpy matplotlib
conda activate nanopore
conda install -c conda-forge -c nanoporetech -c bioconda medaka


Установка вспомогательных программ

Notepad++
https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.7/npp.8.7.Installer.x64.exe


Inkskape
https://inkscape.org/release/inkscape-1.3.2/windows/64-bit/msi/?redirected=1


FileZilla
https://filezilla-project.org/download.php?type=client
