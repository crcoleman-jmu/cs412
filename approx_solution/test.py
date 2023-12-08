import subprocess


for i in range(1, 4):  # Adjust the range based on your actual test cases
    input_file = f"test_cases/input_{i}.txt"
    output_file = f"output_{i}.txt"
    expected_solution_file = f"test_cases/solution_{i}.txt"

    # Run the Python script with the sample input
    command = ["python", "bron_kerbosh.py"]
    with open(input_file, 'r') as input_data, open(output_file, 'w') as output_data:
        subprocess.run(command, stdin=input_data, stdout=output_data, text=True)

    # Display the output
    with open(output_file, 'r') as f:
        print(f"Output for test case {i}:")
        output_content = f.read()
        print(output_content)

    # Compare the output with the expected solution
    with open(expected_solution_file, 'r') as expected_solution_data:
        expected_solution = expected_solution_data.read().strip()

    if output_content.strip() == expected_solution:
        print(f"Test case {i} Passed!")
    else:
        print(f"Test case {i} Failed!")
        print(f"Expected solution: {expected_solution}")
        print(f"Actual output: {output_content}")

    print("--------------------------------------")
