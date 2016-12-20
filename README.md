# Transistor Tools
Code for taking measurements insitu.
To run:
> python3 main_program.py

## Functionality
- IV Sweeps
- Fixed voltage measurements
- Extracts conductivity

## Requirements:
- python3 (anaconda3)
- pyqt4 (conda install qt=4)
- pyvisa (conda install --channel https://conda.anaconda.org/conda-forge pyvisa)
- pyvisa-py (pip install pyvisa-py)
- serial (conda install serial)
- Required group on DAQ comp: 'sudo usermod -a -G GroupName UserName'
