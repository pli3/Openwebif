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
__CHEETAH_genTime__ = 1364979192.08711
__CHEETAH_genTimestamp__ = 'Wed Apr  3 17:53:12 2013'
__CHEETAH_src__ = '/home/fermi/Work/Model/tmsingle/openpli3.0/build-tmsingle/tmp/work/mips32el-oe-linux/enigma2-plugin-extensions-openwebif-0.1+git1+279a2577c3bc6defebd4bf9e61a046dcf7f37c01-r0.72/git/plugin/controllers/views/web/epgsearchrss.tmpl'
__CHEETAH_srcLastModified__ = 'Wed Apr  3 17:10:17 2013'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class epgsearchrss(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(epgsearchrss, self).__init__(*args, **KWs)
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
        
        _orig_filter_65358985 = _filter
        filterName = u'WebSafe'
        if self._CHEETAH__filters.has_key("WebSafe"):
            _filter = self._CHEETAH__currentFilter = self._CHEETAH__filters[filterName]
        else:
            _filter = self._CHEETAH__currentFilter = \
			self._CHEETAH__filters[filterName] = getattr(self._CHEETAH__filtersLib, filterName)(self).filter
        write(u'''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
\t<channel>
\t\t<title>''')
        _v = VFFSL(SL,"title",True) # u'$title' on line 5, col 10
        if _v is not None: write(_filter(_v, rawExpr=u'$title')) # from line 5, col 10.
        write(u'''</title>
\t\t<link>
\t\t\thttp://
\t\t</link>
\t\t<description>''')
        _v = VFFSL(SL,"description",True) # u'$description' on line 9, col 16
        if _v is not None: write(_filter(_v, rawExpr=u'$description')) # from line 9, col 16.
        write(u'''</description>
\t\t<generator>''')
        _v = VFFSL(SL,"generator",True) # u'$generator' on line 10, col 14
        if _v is not None: write(_filter(_v, rawExpr=u'$generator')) # from line 10, col 14.
        write(u'''</generator>
''')
        for event in VFFSL(SL,"events",True): # generated from line 11, col 3
            write(u'''\t\t<item>
\t\t\t<title>''')
            _v = VFFSL(SL,"event.title",True) # u'$event.title' on line 13, col 11
            if _v is not None: write(_filter(_v, rawExpr=u'$event.title')) # from line 13, col 11.
            write(u''' (''')
            _v = VFFSL(SL,"event.date",True) # u'$event.date' on line 13, col 25
            if _v is not None: write(_filter(_v, rawExpr=u'$event.date')) # from line 13, col 25.
            write(u''' ''')
            _v = VFFSL(SL,"event.begin",True) # u'$event.begin' on line 13, col 37
            if _v is not None: write(_filter(_v, rawExpr=u'$event.begin')) # from line 13, col 37.
            write(u''')</title>
\t\t\t<description>
\t\t\t\tService: ''')
            _v = VFFSL(SL,"event.sname",True) # u'$event.sname' on line 15, col 14
            if _v is not None: write(_filter(_v, rawExpr=u'$event.sname')) # from line 15, col 14.
            write(u'''
\t\t\t\t<br/>
\t\t\t\tStart Time: ''')
            _v = VFFSL(SL,"event.date",True) # u'$event.date' on line 17, col 17
            if _v is not None: write(_filter(_v, rawExpr=u'$event.date')) # from line 17, col 17.
            write(u''' ''')
            _v = VFFSL(SL,"event.begin",True) # u'$event.begin' on line 17, col 29
            if _v is not None: write(_filter(_v, rawExpr=u'$event.begin')) # from line 17, col 29.
            write(u'''
\t\t\t\t<br/>
\t\t\t\tDuration: ''')
            _v = VFFSL(SL,"event.duration",True) # u'$event.duration' on line 19, col 15
            if _v is not None: write(_filter(_v, rawExpr=u'$event.duration')) # from line 19, col 15.
            write(u''' minutes
\t\t\t\t<br/>
''')
            if VFFSL(SL,"event.shortdesc",True): # generated from line 21, col 5
                write(u'''\t\t\t\t''')
                _v = VFFSL(SL,"event.shortdesc",True) # u'$event.shortdesc' on line 22, col 5
                if _v is not None: write(_filter(_v, rawExpr=u'$event.shortdesc')) # from line 22, col 5.
                write(u'''
\t\t\t\t<br/>
''')
            write(u'''\t\t\t\t<br/>
\t\t\t\t''')
            _v = VFFSL(SL,"event.longdesc",True) # u'$event.longdesc' on line 26, col 5
            if _v is not None: write(_filter(_v, rawExpr=u'$event.longdesc')) # from line 26, col 5.
            write(u'''
\t\t\t</description>
\t\t\t<author>''')
            _v = VFFSL(SL,"event.sname",True) # u'$event.sname' on line 28, col 12
            if _v is not None: write(_filter(_v, rawExpr=u'$event.sname')) # from line 28, col 12.
            write(u'''</author>
\t\t</item>
''')
        write(u'''   </channel>
</rss>
''')
        _filter = self._CHEETAH__currentFilter = _orig_filter_65358985
        
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

    _mainCheetahMethod_for_epgsearchrss= 'respond'

## END CLASS DEFINITION

if not hasattr(epgsearchrss, '_initCheetahAttributes'):
    templateAPIClass = getattr(epgsearchrss, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(epgsearchrss)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=epgsearchrss()).run()


