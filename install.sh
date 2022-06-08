#!/bin/bash
echo "–––––––––––––––––––––––––––––––––––––––––––––––––––"
echo "Starting Installation"
echo "–––––––––––––––––––––––––––––––––––––––––––––––––––"
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -O ~/miniconda.sh
bash ~/miniconda.sh -b -p $HOME/miniconda
. $HOME/miniconda/bin/activate
yes | conda create --name icbm python=2.7
conda activate icbm
yes | conda install -c anaconda wxpython
yes | conda install -c anaconda numpy
chmod +x run.sh
echo "–––––––––––––––––––––––––––––––––––––––––––––––––––"
echo "Installation Complete"
echo "–––––––––––––––––––––––––––––––––––––––––––––––––––"