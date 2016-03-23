#!/bin/bash
rm  01_USDJPY_D.csv
wget http://dyna.central-tanshifx.com/service/market/csv/01_USDJPY_D.csv
./turtle.py 01_USDJPY_D.csv
