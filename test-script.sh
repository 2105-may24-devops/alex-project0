#! /bin/bash
{ python3 p0.py uno 2 5 
python3 p0.py dos 2 5 3 2 
python3 p0.py tres 6 4 2 
python3 p0.py quatro 7 5 3 
python3 p0.py cinco 1 2 3 
python3 p0.py test6 4 5 s 
} > test-run.txt

if cmp "test-run.txt" "test-cmp.txt"; then
      echo "Tests succeeded"
    else
      echo "Tests failed"
    fi
