import sys
import os

# CSV FIXER

# If you look at the "data/311_Cases_SF.csv", the "Point"
# values aren't wrapped with quotes. So when you parse it,
# the parser views the commas in the coordiates and treats
# it as two values, which shifts all the data to the right.

# This program goes through "data/311_Cases_SF.csv", adds
# the commas before and after the "Point" value and adds it
# to a given output file.

# HOW TO RUN
# 1. copy this script to f25-hw3-AudenGDavis/data/
# 2. run this python script from the terminal with the following arguments
#     $ python data/csvFixer.py -to data/311_Cases_SF_Corrected.csv
#       or 
#     $ python3 data/csvFixer.py -to data/311_Cases_SF_Corrected.csv

# This was written by Auden Davis.

if __name__ == "__main__":
    arguments: list[str] = sys.argv 

    if arguments[0] != "data/csvFixer.py":
        print("ERROR: incorrect python file location")
        print("Please move this python file to \"f25-hw3-AudenGDavis/data/\"")
        sys.exit()


    if len(arguments) < 3 or sys.argv[1] != "-to":
        print("ERROR: invalid arguments")
        print(f"correct format: python {arguments[0]} -to [outputFile]")
        sys.exit()



    in_filePath: str = "data/311_Cases_SF.csv"
    out_filePath: str = sys.argv[2]

    if not os.path.exists(in_filePath):

        print(f"ERROR: file \"{in_filePath}\" not found")
        sys.exit()


    with open(in_filePath, 'r', encoding="utf-8") as infile, open(out_filePath, 'w', encoding="utf-8") as outfile:
        IS_FIRST_LINE: bool = True
        for line in infile:
            if IS_FIRST_LINE:
                IS_FIRST_LINE = False
                outfile.write(line)
                continue

            processed_line: str = ""
            commas: int = 0
            COMMAS_NEEDED: int = 9
            is_done = False


            for char in line:  
                if commas < COMMAS_NEEDED:
                    if char == ",":
                        commas += 1
                    processed_line = processed_line + char

                elif commas >= COMMAS_NEEDED and not is_done:
                    if char == "(":
                        processed_line = processed_line + "\"("
                    elif char == ")":
                        processed_line = processed_line + ")\""
                        is_done = True
                    else:
                        processed_line = processed_line + char

                else:
                    processed_line = processed_line + char

            outfile.write(processed_line)

