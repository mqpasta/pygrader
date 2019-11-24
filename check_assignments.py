import shutil
import os
import sys
import getopt
import glob
import subprocess
import pathlib

def CopyFile(inputfile):
    dst = "std1.py"
    shutil.copyfile(inputfile, dst)

def GetAllSubmissions():
    # get all list of python files in submissions folder
    return glob.glob("submissions/*.py")


def CheckSubmissions(output = "results.txt", isAll = False):
    f = open(output, "w+")
    f.writelines("filename,errors,failures\n")
    f.close()

    filetocall = "python testsuite.py -i "
    
    allSubmissions = GetAllSubmissions()
    for aSubmit in allSubmissions:
        try:
            py_compile.compile(aSubmit, doraise=True)
            CopyFile(aSubmit)
            stem = pathlib.Path(aSubmit).stem
            tocall = filetocall + aSubmit + " -r " + output + " > " + stem+".out"
            print(tocall)
            subprocess.call(tocall)
        except py_compile.PyCompileError:
            stem = pathlib.Path(aSubmit).stem
            f = open(output, "a+")
            f.writelines(stem+" Compile error,Compile Error, Compile Error\n")
            f.close()
            
        if isAll==False:
            ch = input("Do you want to continue (y/n)")
            if ch.lower() != "y":
                break

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"all:o:")
    except getopt.GetoptError:
        print("check_assignment.py -all -o outputfile ")

    isAll = False
    outputfile = "results.txt"
    for opt, arg in opts:
        if opt in ('-all'):
            isAll = True
        if opt in ("-o"):
            outputfile = arg

    CheckSubmissions(isAll = isAll, output = outputfile)  

            


if __name__ == "__main__":
   main(sys.argv[1:])


