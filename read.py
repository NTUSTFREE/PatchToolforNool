import sys, getopt


def main(argv):
    options = "shp"
    long_options = ["show", "rule", "patch"]

    CheckInput()
    
    try:
        opt, values = getopt.getopt(argv, options, long_options)
        for currentArg, currentVal in opt:
            if currentArg in ("-h", "--help"):
                Manual()
                sys.exit()
                
            elif currentArg in ("-s", "--show"):
                ShowRule()
                sys.exit()                
            elif currentArg in ("-p", "--patch"):
                PatchRule()
                sys.exit()
            elif currentArg in (""):
                print("You could get help from python test.py -h")
                sys.exit()
                
    except getopt.GetoptError:
        print("You could get help from python test.py -h")
        sys.exit()
        
def CheckInput():
    n = len(sys.argv)
    if n > 4 or n == 1:
        Manual()
        sys.exit()
        
    for i in range(1, n):
        if sys.argv[i] == "-h":
            continue
        elif sys.argv[i] == "-s":
            continue
        elif sys.argv[i] == "-p":
            continue
        else:  
            Manual()
            sys.exit()
            
def Manual():
    print("##############################################################################")
    print("#                                                                            #")
    print("# Name:                                                                      #")
    print("#       read.py                                                              #")
    print("#                                                                            #")
    print("# Description:                                                               #")
    print("#       A patch tool to upgrage mitre rule in .nool file                     #")
    print("#                                                                            #")
    print("# SYNOPSIS:                                                                  #")
    print("#       python read.py [command] arguments                                   #")
    print("#                                                                            #")
    print("# EXAMPLE:                                                                   #")
    print("#       python test.py -p rule.json               Patch rule to .nool file   #")
    print("#       python test.py -s                         show rule in .nool file    #")
    print("#                                                                            #")
    print("##############################################################################")
    
def PatchRule():
    print("Start to patch rule with Mitre version 9")
    
    
def ShowRule():
    print("Show rule in .nool file")
if __name__ == "__main__":
    main(sys.argv[1:])