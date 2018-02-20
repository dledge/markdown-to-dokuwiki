#!/usr/bin/python
# -*- coding: utf-8 -*-

# This is a VERY bare bones converter from markdown to doku wiki.
#
# Usage:
#   python md2doku.py inputfile.md
# Output will be written to the console so it can be copied and pasted into a dokuwiki

import argparse, sys, re

# Command line arguments
parser = argparse.ArgumentParser(description='Convert markdown (md) to dokuwiki')
parser.add_argument('infile', type=argparse.FileType('r'), help='Input markdown file')

# If no arguments provided, print help
if len(sys.argv)==1:
    parser.print_help()
    sys.exit(1)

# Parse arguments
args = parser.parse_args()

# Get markdown text from input file
mdTxt = args.infile.read()

# Process headers
mdTxt = re.sub(r'###### (.*?) ######', r'= \1=',mdTxt)
mdTxt = re.sub(r'###### (.*?)\n',      r'= \1 =',mdTxt)
mdTxt = re.sub(r'##### (.*?) #####',   r'== \1 ==',mdTxt)
mdTxt = re.sub(r'##### (.*?)\n',       r'== \1 ==',mdTxt)
mdTxt = re.sub(r'#### (.*?) ####',     r'=== \1 ===',mdTxt)
mdTxt = re.sub(r'#### (.*?)\n',        r'=== \1 ===',mdTxt)
mdTxt = re.sub(r'### (.*?) ###',       r'==== \1 ====',mdTxt)
mdTxt = re.sub(r'### (.*?)\n',         r'==== \1 ====',mdTxt)
mdTxt = re.sub(r'## (.*?) ##',         r'===== \1 =====',mdTxt)
mdTxt = re.sub(r'## (.*?)\n',          r'===== \1 =====',mdTxt)
mdTxt = re.sub(r'# (.*?) #',           r'====== \1 ======',mdTxt)
mdTxt = re.sub(r'# (.*?)\n',           r'====== \1 ======',mdTxt)

# Process code
mdTxt = re.sub(r'```(C|javascript|ruby|c|python)',   r'<code>',mdTxt)
mdTxt = re.sub(r'```',   r'</code>',mdTxt)
mdTxt = re.sub(r' `', r' //',mdTxt)
mdTxt = re.sub(r'` ', r'// ',mdTxt)
mdTxt = re.sub(r'([^A-Za-z0-9])`', r'\1//',mdTxt)
mdTxt = re.sub(r'`([^A-Za-z0-9])', r'//\1',mdTxt)

# images
mdTxt = re.sub(r'\!\[(.*?)\]\((.*?)\)',  r'{{\2\|\1}}',mdTxt)

# bold
#mdTxt = re.sub(r'(__)(.+?)(__)', r'**\2**',mdTxt)

# italics
mdTxt = re.sub(r'([^\*])\*{1}([^\*].*?[^\*])\*{1}([^\*])', r'\1//\2//\3',mdTxt)
#mdTxt = re.sub(r'([^_])_(.+?)_([^_])', r'\1//\2//\3',mdTxt)

print(mdTxt)
