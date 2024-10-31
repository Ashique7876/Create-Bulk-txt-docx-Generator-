import os

#Input From User Which File Type He Want

filetype = input("Enter File Type :Like(docx,txt)\n")

#Input From User How Many File He Want
filecount=int(input("Enter How Many File You Want?\n"))

#Input From User Which Path
directory =input("Enter Path\n")

# Starting a loop to create files
for i in range(1,filecount+1):
    file_name = f"file{i}.{filetype}"#Creating a unique file name
    file_path = os.path.join(directory, file_name)#Combining directory path and file name

    # Creating the file
    with open(file_path, "w") as f:
        pass  # Leave the file empty

print(f"Successfully Created {filecount} {filetype} files!!!!!!!!")
