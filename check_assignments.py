import shutil
import os
import sys
import getopt
import glob
import subprocess
import pathlib
import py_compile

def CopyFile(inputfile):
    dst = "std1.py"
    shutil.copyfile(inputfile, dst)

def GetAllSubmissions(inputfile):
    # get all list of python files in submissions folder
    if inputfile == "":
        inputfile = "submissions/*.py"
    
    return glob.glob(inputfile)


def CheckSubmissions(output = "results.txt", isAll = False, inputfile = ""):
    f = open(output, "w+")
    f.writelines("filename,errors,failures\n")
    f.close()

    filetocall = "python testsuite.py -i "
    
    allSubmissions = GetAllSubmissions(inputfile)
    for aSubmit in allSubmissions:
        print("***** starting for ******",aSubmit)
        try:
            py_compile.compile(aSubmit, doraise=True)
            CopyFile(aSubmit)
            stem = pathlib.Path(aSubmit).stem
            tocall = filetocall + aSubmit + " -r " + output + " > " + stem+".out"
            print(tocall)
            subprocess.call(tocall)
        except py_compile.PyCompileError:
            stem = pathlib.Path(aSubmit).stem
            print("***************** COMPILE ERROR ***************",stem)
            f = open(output, "a+")
            f.writelines(stem+" Compile error,Compile Error, Compile Error\n")
            f.close()
        except:
            stem = pathlib.Path(aSubmit).stem
            print("***************** ERROR ***************",stem)
            f = open(output, "a+")
            f.writelines(stem+" Error, Error, Error\n")
            f.close()
        print("***** ending for ******",aSubmit)
        
        if isAll==False:
            ch = input("Do you want to continue (y/n)")
            if ch.lower() != "y":
                break

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"all:o:i:")
    except getopt.GetoptError:
        print("check_assignment.py -all -o outputfile [-i inputfile]")

    isAll = False
    outputfile = "results.txt"
    inputfile = ""
    for opt, arg in opts:
        if opt in ('-all'):
            isAll = True
        if opt in ("-o"):
            outputfile = arg
        if opt in ("-i"):
            inputfile = arg

    CheckSubmissions(isAll = isAll, output = outputfile, inputfile = inputfile)  

            


if __name__ == "__main__":
   main(sys.argv[1:])


