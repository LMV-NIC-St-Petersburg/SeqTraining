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
## Загрузка тестовых данных MIRA

[Скачать тестовые данные MIRA](https://drive.google.com/file/d/1E_-94hdu1l3sKhHySOEk55l1AjXz3Uex/view?usp=sharing)

## Загрузка данных запуска
[Скачать данные запуска №1 (20240926)](https://bit.ly/3ZG5HIR)

## Информация об образцах

| Баркод | Номер образца | Патоген |
| ------ | ------------- | ------- |
| NB01 | 1682 | грипп A |
| NB02 | 1683 | грипп A |
| NB03 | 1684 | грипп A |
| NB04 | 1685 | грипп A |
| NB05 | 1686 | грипп A |
| NB06 | 1687 | грипп A |
| NB07 | 1407 | грипп A |
| NB08 | 1408 | грипп A |
| NB09 | 1409 | грипп A |
| NB10 | 1410 | грипп A |
| NB11 | 1411 | грипп A |
| NB12 | 1412 | грипп A |
| NB13 | 1703 | грипп A |
| NB14 | 1704 | грипп A |
| NB15 | 1705 | грипп A |
| NB16 | 1706 | грипп A |
| NB17 | 1707 | грипп A |
| NB18 | 1708 | грипп A |
| NB19 | 1306 | грипп A |
| NB20 | 1307 | грипп A |
| NB21 | 1308 | грипп A |
| NB22 | 1309 | грипп A |
| NB23 | 1310 | грипп A |
| NB24 | 101 | SARS-CoV-2 |
| NB25 | 99 | SARS-CoV-2 |
| NB26 | 98 | SARS-CoV-2 |
| NB27 | 97 | SARS-CoV-2 |
| NB28 | 145 | SARS-CoV-2 |
| NB29 | 144 | SARS-CoV-2 |
| NB30 | 164 | SARS-CoV-2 |
| NB31 | 163 | SARS-CoV-2 |
| NB32 | 162 | SARS-CoV-2 |
| NB33 | 161 | SARS-CoV-2 |
| NB34 | 160 | SARS-CoV-2 |
| NB35 | 159 | SARS-CoV-2 |
| NB36 | 158 | SARS-CoV-2 |
| NB37 | 194 | SARS-CoV-2 |
| NB38 | 190 | SARS-CoV-2 |
| NB39 | 186 | SARS-CoV-2 |
| NB40 | 173 | SARS-CoV-2 |
| NB41 | 169 | SARS-CoV-2 |
| NB42 | 168 | SARS-CoV-2 |
| NB43 | 255 | SARS-CoV-2 |
| NB44 | 251 | SARS-CoV-2 |
| NB45 | 250 | SARS-CoV-2 |
| NB46 | 249 | SARS-CoV-2 |
| NB47 | 248 | SARS-CoV-2 |
| NB48 | 100 | SARS-CoV-2 |






## Практическое занятие по использованию MIRA


# **День 5**

## Анализ объединенных данных двух запусков MinION с помощью MIRA

[Скачать файл с объединенными данными](https://drive.google.com/file/d/1p058zEu5QlG5hxISuEtuJ6tlPWBYQWHo/view?usp=sharing)

## Практическое занятие по выгрузке данных в EpiFlu GISAID
[Скачать файл для выгрузки данных в GISAID](https://drive.google.com/file/d/1rUlqb5eCA1Jq3i2x0YKUUklPwHNgQKbB/view?usp=sharing)

