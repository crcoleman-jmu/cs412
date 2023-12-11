#!/bin/bash

# Compile and run the Python script
python cs412_maxclique_exact.py > output.txt

# Define sample input
echo "9" > input.txt
echo "a b" >> input.txt
echo "b c" >> input.txt
echo "b d" >> input.txt
echo "d c" >> input.txt
echo "d e" >> input.txt
echo "d f" >> input.txt
echo "f e" >> input.txt
echo "f c" >> input.txt
echo "c e" >> input.txt
echo "c d" >> input.txt
echo "e f" >> input.txt

# Run the script with the sample input
python cs412_maxclique_exact.py < input.txt >> output.txt

# Display the output
cat output.txt

# Compare the output with expected output
expected_output="c d e f"
if [ "$(tail -n 1 output.txt)" == "$expected_output" ]; then
    echo "Test Passed!"
else
    echo "Test Failed!"
fi

# Clean up temporary files
rm input.txt output.txt
