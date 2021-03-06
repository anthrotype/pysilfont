#!/usr/bin/env python 
'''Convert/normalise a UFO.
- If no options are chosen, the output font will simply be a normalised version of the font.'''
__url__ = 'http://github.com/silnrsi/pysilfont'
__copyright__ = 'Copyright (c) 2015, SIL International  (http://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'David Raymond'
__version__ = '0.0.1'

from silfont.genlib import *
from silfont.UFOlib import *

argspec = [
    ('ifont',{'help': 'Input font file'}, {'type': 'infont'}),
    ('ofont',{'help': 'Output font file','nargs': '?' }, {'type': 'outfont', 'def': '_conv'}),
    ('-v','--version',{'help': 'UFO version to output'},{}),
    ('-p','--params',{'help': 'Font output parameters','action': 'append'}, {'type': 'optiondict'})]

def doit(args) :
    font = args.ifont
    params = args.params
    if args.version: params["UFOversion"] = args.version
    # Set output parameters for the font
    fontparams = font.outparams
    for param in params:
        if param in fontparams:
            if param == "UFOversion" and params[param] not in ("2","3"):
                print "UFO version must be 2 or 3"
                sys.exit()
            fontparams[param] = params[param]
        else:
            print "Output parameter invalid:",param
            sys.exit()
                
    return args.ifont
    
execute("PSFU",doit, argspec)