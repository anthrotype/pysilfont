#!/usr/bin/env python
'FontForge: List all the data in a glyph object in key, value pairs'
__url__ = 'http://github.com/silnrsi/pysilfont'
__copyright__ = 'Copyright (c) 2014, SIL International  (http://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'David Raymond'
__version__ = '0.0.1'

import fontforge, types, sys
from silfont.framework import execute

argspec = [
    ('font',{'help': 'Input font file'}, {'type': 'infont'}),
    ('-o','--output',{'help': 'Output text file'}, {'type': 'outfile', 'def': 'glyphinfo.txt'})]


def doit(args) :
    font=args.font
    outf = args.output

    glyphn = raw_input("Glyph name or number: ")

    while glyphn:

        isglyph=True
        if not(glyphn in font):
            try:
                glyphn=int(glyphn)
            except ValueError:
                isglyph=False
            else:
                if not(glyphn in font):
                    isglyph=False

        if isglyph:
            g=font[glyphn]
            outf.write("\n%s\n\n" % glyphn)
            # Write to file all normal key,value pairs - exclude __ and built in functions
            for k in dir(g):
                if k[0:2] == "__": continue
                attrk=getattr(g,k)
                if attrk is None: continue
                tk=type(attrk)
                if tk == types.BuiltinFunctionType: continue
                if k == "ttinstrs": # ttinstr values are not printable characters
                    outf.write("%s,%s\n" % (k,"<has values>"))
                else:
                    outf.write("%s,%s\n" % (k,attrk))
            # Write out all normal keys where value is none
            for k in dir(g):
                attrk=getattr(g,k)
                if attrk is None:
                    outf.write("%s,%s\n" % (k,attrk))
        else:
            print "Invalid glyph"

        glyphn = raw_input("Glyph name or number: ")
    print "done"
    outf.close

execute("FF",doit, argspec)
