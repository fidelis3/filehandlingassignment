#file creation
#create and write to the file
with open("my_file.txt","w") as file:
  file.write("i am fidelis\n")
  file.write("this is line:3\n")
  file.write("i love my dad\n")
  print("file created and lines written successfully")
#file reading and display
with open("my_file.txt","r") as file:
  contents=file.read()
  print("file contents:\n",contents)
#file appending
with open("my_file.txt","a") as file:
  file.write("my second name is ntoiti.\n")
  file.write("my favourite person is victor.\n")
  file.write("i have a twin.\n")
  print("additional lines")
#display contents after appending
with open("my_file.txt","r") as file:
    contents=file.read()
    print("contents after adding:\n",contents)
print("file handling operations completed.")


    
 