#!/bin/bash
# Usage: ./batch_process.sh <lang>

mylist=(lc0a lc0b lc0c lc1 lc1b lc2 lc3 jp1 lc4 lc5 lc6 lc7a lc7b lc8 lc9a lc9b lc10 lc11 lc12 lc13 lc15 lc16 lc17 fr1 fr2 fr3a fr3b fr4a fr4b fr5a fr5b fr6 fr7 fr8 ex1 ex2a ex2b ex3a ex3b ex4 ex5a ex5b ex6 ex7 ex8 ex9 ex10 ex11 pr1 pr2 pr3 lm1 lm1a lm1b)

for l in ${mylist[*]}
do
	echo "$1: $l" >> /tmp/processedgroups.log
	python3 process_data.py $l $1
done



