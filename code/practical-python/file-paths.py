# this is for practising file paths 
# .. - for going out one step 
# / - for going in one step
import os 

curr_dir = os.getcwd()
print(curr_dir)

if os.path.exists("data/sample.txt"):
    print("✅/data/sample.txt exists")
else:
    print("❌/data/sample.txt doesn't exists")


if os.path.exists("../../sample-data1.txt"):
    print("✅Yes file exists in the root dir")
else:
    print("❌Oops! file doesn't exists in the root dir")