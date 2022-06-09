#!/bin/bash
echo "–––––––––––––––––––––––––––––––––––––––––––––––––––"
echo "Starting Installation"
echo "–––––––––––––––––––––––––––––––––––––––––––––––––––"
bash miniconda.sh -b -p $HOME/miniconda
. $HOME/miniconda/bin/activate
yes | conda create --name icbm python=2.7
conda activate icbm
yes | conda install -c anaconda wxpython
yes | conda install -c anaconda numpy
chmod +x run.sh
echo "–––––––––––––––––––––––––––––––––––––––––––––––––––"
echo "Installation Complete"
echo "–––––––––––––––––––––––––––––––––––––––––––––––––––"