#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import sys
import re
def convertfile( mdTxt ):

    #print(mdTxt)
    # Headers
    mdTxt = re.sub(r'##### (.*?) #####',r'== \1 ==',mdTxt)
    mdTxt = re.sub(r'##### (.*?)\n',    r'== \1 ==',mdTxt)

    mdTxt = re.sub(r'#### (.*?) ####',  r'=== \1 ===',mdTxt)
    mdTxt = re.sub(r'#### (.*?)\n',     r'=== \1 ===',mdTxt)
    mdTxt = re.sub(r'### (.*?) ###',    r'==== \1 ====',mdTxt)
    mdTxt = re.sub(r'### (.*?)\n',      r'==== \1 ====',mdTxt)
    mdTxt = re.sub(r'## (.*?) ##',      r'===== \1 =====',mdTxt)
    mdTxt = re.sub(r'# (.*?) #',        r'====== \1 ======',mdTxt)
    mdTxt = re.sub(r'# (.*?) \n',       r'====== \1 ======',mdTxt)

    # code
    mdTxt = re.sub(r'```C',   r'<code>',mdTxt)
    mdTxt = re.sub(r'```',   r'</code>',mdTxt)
    mdTxt = re.sub(r' `', r' //',mdTxt)
    mdTxt = re.sub(r'` ', r'// ',mdTxt)
    mdTxt = re.sub(r'([^A-Za-z0-9])`', r'\1//',mdTxt)
    mdTxt = re.sub(r'`([^A-Za-z0-9])', r'//\1',mdTxt)

    # images
    mdTxt = re.sub(r'\!\[(.*?)\]\((.*?)\)',  r'{{\2\|\1}}',mdTxt)

    print(mdTxt)

    return


# Command line arguments
parser = argparse.ArgumentParser(description='Convert markdown (md) to dokuwiki')
parser.add_argument('infile', type=argparse.FileType('r'), help='Input markdown file')

args = parser.parse_args()

if args.infile:
    convertfile(args.infile.read())
else:
    parser.print_help()
