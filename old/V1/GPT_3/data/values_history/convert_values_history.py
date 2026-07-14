# open the input file for reading
input_file = open("values_history.txt", "r")

# open the output file for writing
output_file = open("converted_cleaned_values_history.txt", "w")

# loop through each line in the input file
for line in input_file:
    # check if the line is contained in brackets or starts with 'Iteration'
    if line.isspace()!=True and (line.startswith("['m") or line.startswith("['t") or line.startswith("['c") or line.startswith("['i") or line.startswith("Iteration") or line.startswith("1") or line.startswith("2") or line.startswith("3") or line.startswith("4") or (line.startswith("5") and line.startswith("500") != True) or line.startswith("6") or line.startswith("7") or line.startswith(" 1") or line.startswith(" 2") or line.startswith(" 3") or line.startswith(" 4") or (line.startswith(" 5") and line.startswith(" 500") != True) or line.startswith(" 6") or line.startswith(" 7")):
    # write the line to the output file
        output_file.write(line)

# close both files
input_file.close()
output_file.close()