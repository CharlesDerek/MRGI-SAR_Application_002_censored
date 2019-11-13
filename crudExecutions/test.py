import subprocess

subprocess.run(["cat","banner.mrgi"])

#subprocess.run(["ls", "-l"])
#Works with commands separated within the list
subprocess.run(["rm","-rf","testFolder/"])
subprocess.run(["echo","testFolder was successfully removed!"])
