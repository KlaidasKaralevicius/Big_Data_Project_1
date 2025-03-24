# Big Data Project Nr.1
Create program using MapReduce approach to extract data from semi-structured .txt file

## File explanation
- **LD1_data.zip** holds data .txt files used for the project
- **mapper1.py** is mapping function for project 1-st and 2-nd part
- **reducer1.py** is reduce functino for project 1-st and 2-nd part
- **write_to_excel1.py** writes .txt output from reducer to .xlsx file
- **run_pipeline1.sh** runs whole process + tracks time it takes to complete the job
- **reduce_output1_raw.txt** outputs reducer1.py data in txt file
- **reduce_output1.xlsx** shows reducer1.py output data in excel document

**shuffle.py** is common function for both parts to shuffle data

**mapper2.py**, **reducer2.py**, **write_to_excel2.py**, **run_pipeline2.sh**, **reduce_output2_raw.txt** and **reduce_output2.xlsx** is same as previous files, but for 3-d part

## Timing
### First hardware
- first part (run_pipeline1.sh) took **29 seconds** to complete on:
    - Windows 10 (git bash terminal)    
    - AMD Ryzen 5 5600 (6 cores, 12 threads, base speed 3,50 GHz)
    - 32 GB RAM (3600 MHz)
    - Nvidia RTX 3060 GPU
    - NVMe disk (PCIe 4.0)
- second part (run_pipeline2.sh) took **29 seconds** aswell to complete on same hardware
### Second hardware
- first part (run_pipeline1.sh) took **9 seconds** to complete on:
    -  Linux Mint (native bash terminal)
    -  AMD Ryzen 5 PRO 3500U (4 cores, 8 threads, base speed 2,1 GHz)
    -  16 GB RAM (2666 MHz)
    -  Integrated graphics
- second part (run_pipeline2.sh) took **8 seconds** to complete on same hardware

- first part took **31 seconds** to complete on:
    - same hardware, Windows 11
- second part took **31 seconds** aswell 
### P.S.
Second hardware is far less powersull, but performs significantly faster, possible cause, OS (Linux vs Windows) have very significant impact

## Extra info
- **run_pipeline** is script written to run on Windows git bash (for linux 'python' need to be changed to 'python3')
- **write_to_excel** needs *openpyxl* which can be installed running - pip install openpyxl
- writing from text file to excel is not calculated in the completion time
