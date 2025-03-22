# Big Data Project Nr.1
Create program using MapReduce approach to extract data from semi-structured .txt file

### File explanation
**mapper1.py** is mapping function for projects 1-st and 2-nd part
**reducer1.py** is reduce functino for projects 1-st and 2-nd part
**write_to_excel1.py** writes .txt output from reducer to .xlsx file
**run_pipeline1.sh** runs whole process + tracks time it takes to complete the job
**reducer1.xlsx** shows reducer1.py output data in excel document

**shuffle.py** is common function for both parts to shuffle data

**mapper2.py**, **reducer2.py**, **write_to_excel2.py**, **run_pipeline2.sh** and **reducer2.xlsx** is same as previous files, but for 3-d part

### Extra info
**run_pipeline** is script written to run on Linux (or using git bash in Windows)
**write_to_excel** needs *openpyxl* which can be installed running - pip install openpyxl
