#!/bin/bash
start_time=$(date +%s)
cat duom_full.txt | python mapper1.py | python shuffle.py | python reducer1.py > reduce_output1_raw.txt
end_time=$(date +%s)
execution_time=$((end_time - start_time))
echo "Execution time: $execution_time seconds"
python write_to_excel1.py