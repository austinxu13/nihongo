# Streamline processing latex document
# Author: Ao Xu

import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--nobib", help="no bib citations",
                    action="store_true")
parser.add_argument("-c", "--clean", help="remove temporary files",
                    action="store_true")
args = parser.parse_args()

# name of the main latex file (do not include .tex)
MAIN = 'main'
# name of the target (something descriptive)
TARGET = '笔记'
# name of command to perform Latex (either pdflatex or latex)
#LATEX = 'pdflatex'
LATEX = 'xelatex'
# name of extensions
FIGEXT  = '.pdf'
MAINEXT = '.pdf'
# define output (could be making .ps instead)
OUTPUT = '{0}{1}'.format(TARGET,MAINEXT)

# typeset
BUILDCOMMAND = 'rm -f {0}.aux'.format(MAIN)
BUILDCOMMAND += ' && {0} {1}'.format(LATEX,MAIN)
#if not args.nobib:
#    BUILDCOMMAND += ' && bibtex {0}'.format(MAIN)
BUILDCOMMAND += ' && {0} {1}'.format(LATEX,MAIN)
BUILDCOMMAND += ' && {0} {1}'.format(LATEX,MAIN)

# clean
CLEAN = 'rm -f *~ *.aux *.log *.bbl *.blg *.dvi *.tmp *.out *.blg *.bbl'
CLEAN += ' {0} {1}{2} {1}.ps'.format(OUTPUT,MAIN,MAINEXT)

if args.clean:
    os.system( CLEAN )
else:
    # do latex twice to make sure that all cross-references are updated
    os.system( BUILDCOMMAND )
    # cp temporary main.pdf to target.
    os.system( 'cp {0}{1} {2}'.format(MAIN,MAINEXT,OUTPUT) )
