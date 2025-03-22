# Big Data Project Nr.1
Create program using MapReduce approach to extract data from semi-structured .txt file

### File explanation
- **mapper1.py** is mapping function for project 1-st and 2-nd part
- **reducer1.py** is reduce functino for project 1-st and 2-nd part
- **write_to_excel1.py** writes .txt output from reducer to .xlsx file
- **run_pipeline1.sh** runs whole process + tracks time it takes to complete the job
- **reduce_output1_raw.txt** outputs reducer1.py data in txt file
- **reduce_output1.xlsx** shows reducer1.py output data in excel document

**shuffle.py** is common function for both parts to shuffle data

**mapper2.py**, **reducer2.py**, **write_to_excel2.py**, **run_pipeline2.sh**, **reduce_output2_raw.txt** and **reduce_output2.xlsx** is same as previous files, but for 3-d part

### Timing
first part (run_pipeline1.sh) took **28** seconds to complete on:
    - 6 core AMD 5th processor (base speed 3,50 GHz)
    - 32 GB RAM (3600 MHz)
    - RTX 3060 GPU
    - NVMe disk (PCIe 4.0)

### Extra info
- **run_pipeline** is script written to run on Linux (or using git bash in Windows)
- **write_to_excel** needs *openpyxl* which can be installed running - pip install openpyxl