#!/usr/bin/env python

"""template_script.py: Template python script."""

__author__     = "Can Bal"
__copyright__  = "Copyright 2015"
__credits__    = ["Can Bal"]

__maintainer__ = "Can Bal"
__email__      = "invalid@email.com"
__version__    = "0.0.1"
__status__     = "Development"

__date__       = "2015-10-09"


# import statements
from argparse import ArgumentParser
from operator import itemgetter
import sys, os, re, glob, csv, signal, shutil

# function definitions
def error(msg, prog=None):
    if prog is None:
        print "error: %s" %msg
    else:
        print "%s: error: %s" %(prog, msg)
    sys.exit(-1)

def warning(msg, prog=None):
    if prog is None:
        print "warning: %s" %msg
    else:
        print "%s: warning: %s" %(prog, msg)

def sigint_handler(signal, frame):
    print ' Interrupted!'
    sys.exit(0)

def ask_confirmation(question, prog=None):
    confirm = raw_input(question + " (yes, no[default]): ")
    if confirm.lower() == 'yes':
        return True
    elif confirm.lower() == 'no' or confirm.lower() == '':
        return False
    else:
        warning("unrecognized answer: " + confirm, prog)
        return ask_confirmation(question, prog)

# main function
def main(argv=None):
    if argv is None:
        argv = sys.argv

    # quit gracefully when Ctrl+C interrupt is received
    signal.signal(signal.SIGINT, sigint_handler)

    # parse command line options
    parser = ArgumentParser(description="Template Python Script - v"+str(__version__))
    parser.add_argument("infile", type=str, help="input file")
    parser.add_argument("outdir", type=str, help="output folder")
    args = parser.parse_args()

    # check if input file exists
    if not os.path.isfile(args.infile):
        error(args.infile + " does not exist")

    # check if output directory exists
    if not os.path.isdir(args.outdir):
        warning(args.outdir + " does not exist!")
        if not ask_confirmation("Do you want to create %s and continue?" %args.outdir):
            sys.exit(0)
        os.makedirs(args.outdir)

    # open file and do something
    try:
        f = open(args.infile, 'r')
    except IOError:
        error(args.infile + " could not be opened!")
    else:
        f.close()

if __name__ == "__main__":
    sys.exit(main())
