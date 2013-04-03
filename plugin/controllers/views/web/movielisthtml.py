#!/usr/bin/env python




##################################################
## DEPENDENCIES
import sys
import os
import os.path
try:
    import builtins as builtin
except ImportError:
    import __builtin__ as builtin
from os.path import getmtime, exists
import time
import types
from Cheetah.Version import MinCompatibleVersion as RequiredCheetahVersion
from Cheetah.Version import MinCompatibleVersionTuple as RequiredCheetahVersionTuple
from Cheetah.Template import Template
from Cheetah.DummyTransaction import *
from Cheetah.NameMapper import NotFound, valueForName, valueFromSearchList, valueFromFrameOrSearchList
from Cheetah.CacheRegion import CacheRegion
import Cheetah.Filters as Filters
import Cheetah.ErrorCatchers as ErrorCatchers

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '2.4.4'
__CHEETAH_versionTuple__ = (2, 4, 4, 'development', 0)
__CHEETAH_genTime__ = 1364979192.163994
__CHEETAH_genTimestamp__ = 'Wed Apr  3 17:53:12 2013'
__CHEETAH_src__ = '/home/fermi/Work/Model/tmsingle/openpli3.0/build-tmsingle/tmp/work/mips32el-oe-linux/enigma2-plugin-extensions-openwebif-0.1+git1+279a2577c3bc6defebd4bf9e61a046dcf7f37c01-r0.72/git/plugin/controllers/views/web/movielisthtml.tmpl'
__CHEETAH_srcLastModified__ = 'Wed Apr  3 17:10:17 2013'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class movielisthtml(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(movielisthtml, self).__init__(*args, **KWs)
        if not self._CHEETAH__instanceInitialized:
            cheetahKWArgs = {}
            allowedKWs = 'searchList namespaces filter filtersLib errorCatcher'.split()
            for k,v in KWs.items():
                if k in allowedKWs: cheetahKWArgs[k] = v
            self._initCheetahInstance(**cheetahKWArgs)
        

    def respond(self, trans=None):



        ## CHEETAH: main method generated for this template
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        _orig_filter_45759429 = _filter
        filterName = u'WebSafe'
        if self._CHEETAH__filters.has_key("WebSafe"):
            _filter = self._CHEETAH__currentFilter = self._CHEETAH__filters[filterName]
        else:
            _filter = self._CHEETAH__currentFilter = \
			self._CHEETAH__filters[filterName] = getattr(self._CHEETAH__filtersLib, filterName)(self).filter
        write(u'''<?xml version="1.0" encoding="UTF-8"?>
<html>
<head>
\t<title>
\t\tEnigma2 Movielist
\t</title>
\t<link/>
</head>
<body>
\t<table>
''')
        for movie in VFFSL(SL,"movies",True): # generated from line 12, col 3
            write(u'''\t\t<tr>
\t\t\t<td class="pageHeader">
\t\t\t\t''')
            _v = VFFSL(SL,"movie.eventname",True) # u'$movie.eventname' on line 15, col 5
            if _v is not None: write(_filter(_v, rawExpr=u'$movie.eventname')) # from line 15, col 5.
            write(u'''
\t\t\t</td>
\t\t</tr>
\t\t<tr>
\t\t\t<td>
\t\t\t\t<b>Description:</b>
\t\t\t\t''')
            _v = VFFSL(SL,"movie.description",True) # u'$movie.description' on line 21, col 5
            if _v is not None: write(_filter(_v, rawExpr=u'$movie.description')) # from line 21, col 5.
            write(u'''
\t\t\t\t<br/>
\t\t\t\t<b>Extended:</b>
\t\t\t\t''')
            _v = VFFSL(SL,"movie.descriptionExtended",True) # u'$movie.descriptionExtended' on line 24, col 5
            if _v is not None: write(_filter(_v, rawExpr=u'$movie.descriptionExtended')) # from line 24, col 5.
            write(u'''
\t\t\t\t<br/>
\t\t\t\t<b>Recording Time:</b>
\t\t\t\t''')
            _v = VFFSL(SL,"movie.begintime",True) # u'$movie.begintime' on line 27, col 5
            if _v is not None: write(_filter(_v, rawExpr=u'$movie.begintime')) # from line 27, col 5.
            write(u'''
\t\t\t\t<br/>
\t\t\t\t<b>Tags:</b>
\t\t\t\t''')
            _v = VFFSL(SL,"movie.tags",True) # u'$movie.tags' on line 30, col 5
            if _v is not None: write(_filter(_v, rawExpr=u'$movie.tags')) # from line 30, col 5.
            write(u'''
\t\t\t\t<br/>
\t\t\t\t<b>Channel:</b>
\t\t\t\t''')
            _v = VFFSL(SL,"movie.servicename",True) # u'$movie.servicename' on line 33, col 5
            if _v is not None: write(_filter(_v, rawExpr=u'$movie.servicename')) # from line 33, col 5.
            write(u'''
\t\t\t</td>
\t\t</tr>
\t\t<tr height="20">
\t\t\t<td>
\t\t\t</td>
\t\t</tr>
''')
        write(u'''\t</table>
</body>
</html>
''')
        _filter = self._CHEETAH__currentFilter = _orig_filter_45759429
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        
    ##################################################
    ## CHEETAH GENERATED ATTRIBUTES


    _CHEETAH__instanceInitialized = False

    _CHEETAH_version = __CHEETAH_version__

    _CHEETAH_versionTuple = __CHEETAH_versionTuple__

    _CHEETAH_genTime = __CHEETAH_genTime__

    _CHEETAH_genTimestamp = __CHEETAH_genTimestamp__

    _CHEETAH_src = __CHEETAH_src__

    _CHEETAH_srcLastModified = __CHEETAH_srcLastModified__

    _mainCheetahMethod_for_movielisthtml= 'respond'

## END CLASS DEFINITION

if not hasattr(movielisthtml, '_initCheetahAttributes'):
    templateAPIClass = getattr(movielisthtml, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(movielisthtml)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=movielisthtml()).run()


