#!/usr/bin/env python
'FontForge: Remove overlap on all glyphs in font'
__url__ = 'http://github.com/silnrsi/pysilfont'
__copyright__ = 'Copyright (c) 2014, SIL International  (http://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'Victor Gaultney'
__version__ = '0.0.1'

from silfont.framework import execute

argspec = [
    ('ifont',{'help': 'Input font file'}, {'type': 'infont'}),
    ('ofont',{'help': 'Output font file','nargs': '?' }, {'type': 'outfont', 'def': 'new'})]

def doit(args) :
    font = args.ifont
    for glyph in font:
        font[glyph].removeOverlap()
    return font

execute("FF",doit,argspec)
