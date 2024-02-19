# mr-Ucar
# Simple Multi File Renamer Project for my own needs
# I have a bunch of files that I want to rename in a specific way.
# The files are named int1.pdf, int2.pdf, int3.pdf, and so on.
# I want to rename them to Speaking Booklet Unit1.pdf, Speaking Booklet Unit2.pdf, Speaking Booklet Unit3.pdf, and so on.
# I can use the os module to rename the files.


import os

# Directory containing the files
directory = "D:\\Ydy 2024\\Github Desktop icin\\2nd Term\\2023-2024\\Resources\\2024 - 2nd Term RESOURCES\\2nd Term\\Speaking\\Resources\\INTERMEDIATE"

# Iterate over the files in the directory
for filename in os.listdir(directory):
    if filename.startswith("int") and filename.endswith(".pdf"):
        # Extract the number from the filename
        number = filename[3:-4]

        # Construct the new filename
        new_filename = f"Speaking Booklet Unit{number}.pdf"

        # Rename the file
        os.rename(
            os.path.join(directory, filename), os.path.join(directory, new_filename)
        )
