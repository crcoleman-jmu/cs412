#!/bin/bash

# Compile and run the Python script for each test case
for i in {1..3}; do
    echo "Running test case $i..."
    
    # Define input and output file paths
    input_file="test_cases/input_$i.txt"
    output_file="output_$i.txt"

    # Generate or define sample input
    # You can modify this part based on your actual test cases
    echo "Sample input for test case $i" > "$input_file"
    # Add more echo commands to populate the input file
    
    # Run the Python script with the sample input
    python bron_kerbosh.py < "$input_file" > "$output_file"

    # Display the output
    echo "Output for test case $i:"
    cat "$output_file"

    # Clean up temporary files
    rm "$input_file" "$output_file"

    echo "--------------------------------------"
done
