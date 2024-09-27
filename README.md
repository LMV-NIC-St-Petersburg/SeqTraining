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



# **День 4**

## Загрузка данных запуска
[Скачать данные запуска №1 (20240926)](https://bit.ly/3ZG5HIR)

## Информация об образцах

| Баркод | Номер образца | Патоген |
| ------ | ------------- | ------- |
| NB01 | 1682 | SARS-CoV-2 |
| NB02 | 1683 | SARS-CoV-2 |
| NB03 | 1684 | SARS-CoV-2 |
| NB04 | 1685 | SARS-CoV-2 |
| NB05 | 1686 | SARS-CoV-2 |
| NB06 | 1687 | SARS-CoV-2 |
| NB07 | 1407 | SARS-CoV-2 |
| NB08 | 1408 | SARS-CoV-2 |
| NB09 | 1409 | SARS-CoV-2 |
| NB10 | 1410 | SARS-CoV-2 |
| NB11 | 1411 | SARS-CoV-2 |
| NB12 | 1412 | SARS-CoV-2 |
| NB13 | 1703 | SARS-CoV-2 |
| NB14 | 1704 | SARS-CoV-2 |
| NB15 | 1705 | SARS-CoV-2 |
| NB16 | 1706 | SARS-CoV-2 |
| NB17 | 1707 | SARS-CoV-2 |
| NB18 | 1708 | SARS-CoV-2 |
| NB19 | 1306 | SARS-CoV-2 |
| NB20 | 1307 | SARS-CoV-2 |
| NB21 | 1308 | SARS-CoV-2 |
| NB22 | 1309 | SARS-CoV-2 |
| NB23 | 1310 | SARS-CoV-2 |
| NB24 | 101 | грипп А |
| NB25 | 99 | грипп А |
| NB26 | 98 | грипп А |
| NB27 | 97 | грипп А |
| NB28 | 145 | грипп А |
| NB29 | 144 | грипп А |
| NB30 | 164 | грипп А |
| NB31 | 163 | грипп А |
| NB32 | 162 | грипп А |
| NB33 | 161 | грипп А |
| NB34 | 160 | грипп А |
| NB35 | 159 | грипп А |
| NB36 | 158 | грипп А |
| NB37 | 194 | грипп А |
| NB38 | 190 | грипп А |
| NB39 | 186 | грипп А |
| NB40 | 173 | грипп А |
| NB41 | 169 | грипп А |
| NB42 | 168 | грипп А |
| NB43 | 255 | грипп А |
| NB44 | 251 | грипп А |
| NB45 | 250 | грипп А |
| NB46 | 249 | грипп А |
| NB47 | 248 | грипп А |
| NB48 | 100 | грипп А |






## Практическое занятие по использованию MIRA

