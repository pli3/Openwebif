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
__CHEETAH_genTime__ = 1364979192.143875
__CHEETAH_genTimestamp__ = 'Wed Apr  3 17:53:12 2013'
__CHEETAH_src__ = '/home/fermi/Work/Model/tmsingle/openpli3.0/build-tmsingle/tmp/work/mips32el-oe-linux/enigma2-plugin-extensions-openwebif-0.1+git1+279a2577c3bc6defebd4bf9e61a046dcf7f37c01-r0.72/git/plugin/controllers/views/web/getcurrent.tmpl'
__CHEETAH_srcLastModified__ = 'Wed Apr  3 17:10:17 2013'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class getcurrent(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(getcurrent, self).__init__(*args, **KWs)
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
        
        _orig_filter_47255804 = _filter
        filterName = u'WebSafe'
        if self._CHEETAH__filters.has_key("WebSafe"):
            _filter = self._CHEETAH__currentFilter = self._CHEETAH__filters[filterName]
        else:
            _filter = self._CHEETAH__currentFilter = \
			self._CHEETAH__filters[filterName] = getattr(self._CHEETAH__filtersLib, filterName)(self).filter
        write(u'''<?xml version="1.0" encoding="UTF-8"?>
<e2currentserviceinformation>
\t<e2service>
\t\t<e2servicereference>''')
        _v = VFFSL(SL,"info.ref",True) # u'$info.ref' on line 5, col 23
        if _v is not None: write(_filter(_v, rawExpr=u'$info.ref')) # from line 5, col 23.
        write(u'''</e2servicereference>
\t\t<e2servicename>''')
        _v = VFFSL(SL,"info.name",True) # u'$info.name' on line 6, col 18
        if _v is not None: write(_filter(_v, rawExpr=u'$info.name')) # from line 6, col 18.
        write(u'''</e2servicename>
\t\t<e2providername>''')
        _v = VFFSL(SL,"info.provider",True) # u'$info.provider' on line 7, col 19
        if _v is not None: write(_filter(_v, rawExpr=u'$info.provider')) # from line 7, col 19.
        write(u'''</e2providername>
\t\t<e2videowidth>''')
        _v = VFFSL(SL,"info.width",True) # u'$info.width' on line 8, col 17
        if _v is not None: write(_filter(_v, rawExpr=u'$info.width')) # from line 8, col 17.
        write(u'''</e2videowidth>
\t\t<e2videoheight>''')
        _v = VFFSL(SL,"info.height",True) # u'$info.height' on line 9, col 18
        if _v is not None: write(_filter(_v, rawExpr=u'$info.height')) # from line 9, col 18.
        write(u'''</e2videoheight>
\t\t<e2servicevideosize>''')
        _v = VFFSL(SL,"info.width",True) # u'${info.width}' on line 10, col 23
        if _v is not None: write(_filter(_v, rawExpr=u'${info.width}')) # from line 10, col 23.
        write(u'''x''')
        _v = VFFSL(SL,"info.height",True) # u'${info.height}' on line 10, col 37
        if _v is not None: write(_filter(_v, rawExpr=u'${info.height}')) # from line 10, col 37.
        write(u'''</e2servicevideosize>
\t\t<e2iswidescreen>
''')
        if VFFSL(SL,"info.iswidescreen",True) : # generated from line 12, col 4
            _v =  "1" 
            if _v is not None: write(_filter(_v))
        else:
            _v =  "0"
            if _v is not None: write(_filter(_v))
        write(u'''\t\t</e2iswidescreen>
\t\t<e2apid>''')
        _v = VFFSL(SL,"info.apid",True) # u'$info.apid' on line 14, col 11
        if _v is not None: write(_filter(_v, rawExpr=u'$info.apid')) # from line 14, col 11.
        write(u'''</e2apid>
\t\t<e2vpid>''')
        _v = VFFSL(SL,"info.vpid",True) # u'$info.vpid' on line 15, col 11
        if _v is not None: write(_filter(_v, rawExpr=u'$info.vpid')) # from line 15, col 11.
        write(u'''</e2vpid>
\t\t<e2pcrpid>''')
        _v = VFFSL(SL,"info.pcrpid",True) # u'$info.pcrpid' on line 16, col 13
        if _v is not None: write(_filter(_v, rawExpr=u'$info.pcrpid')) # from line 16, col 13.
        write(u'''</e2pcrpid>
\t\t<e2pmtpid>''')
        _v = VFFSL(SL,"info.pmtpid",True) # u'$info.pmtpid' on line 17, col 13
        if _v is not None: write(_filter(_v, rawExpr=u'$info.pmtpid')) # from line 17, col 13.
        write(u'''</e2pmtpid>
\t\t<e2txtpid>''')
        _v = VFFSL(SL,"info.txtpid",True) # u'$info.txtpid' on line 18, col 13
        if _v is not None: write(_filter(_v, rawExpr=u'$info.txtpid')) # from line 18, col 13.
        write(u'''</e2txtpid>
\t\t<e2tsid>''')
        _v = VFFSL(SL,"info.tsid",True) # u'$info.tsid' on line 19, col 11
        if _v is not None: write(_filter(_v, rawExpr=u'$info.tsid')) # from line 19, col 11.
        write(u'''</e2tsid>
\t\t<e2onid>''')
        _v = VFFSL(SL,"info.onid",True) # u'$info.onid' on line 20, col 11
        if _v is not None: write(_filter(_v, rawExpr=u'$info.onid')) # from line 20, col 11.
        write(u'''</e2onid>
\t\t<e2sid>''')
        _v = VFFSL(SL,"info.sid",True) # u'$info.sid' on line 21, col 10
        if _v is not None: write(_filter(_v, rawExpr=u'$info.sid')) # from line 21, col 10.
        write(u'''</e2sid>
\t</e2service>
\t<e2eventlist>
\t\t<e2event>
\t\t\t<e2eventservicereference>''')
        _v = VFFSL(SL,"now.sref",True) # u'$now.sref' on line 25, col 29
        if _v is not None: write(_filter(_v, rawExpr=u'$now.sref')) # from line 25, col 29.
        write(u'''</e2eventservicereference>
\t\t\t<e2eventservicename>''')
        _v = VFFSL(SL,"now.sname",True) # u'$now.sname' on line 26, col 24
        if _v is not None: write(_filter(_v, rawExpr=u'$now.sname')) # from line 26, col 24.
        write(u'''</e2eventservicename>
\t\t\t<e2eventprovidername>''')
        _v = VFFSL(SL,"now.provider",True) # u'$now.provider' on line 27, col 25
        if _v is not None: write(_filter(_v, rawExpr=u'$now.provider')) # from line 27, col 25.
        write(u'''</e2eventprovidername>
\t\t\t<e2eventid>''')
        _v = VFFSL(SL,"now.id",True) # u'$now.id' on line 28, col 15
        if _v is not None: write(_filter(_v, rawExpr=u'$now.id')) # from line 28, col 15.
        write(u'''</e2eventid>
\t\t\t<e2eventname>''')
        _v = VFFSL(SL,"now.title",True) # u'$now.title' on line 29, col 17
        if _v is not None: write(_filter(_v, rawExpr=u'$now.title')) # from line 29, col 17.
        write(u'''</e2eventname>
\t\t\t<e2eventtitle>''')
        _v = VFFSL(SL,"now.title",True) # u'$now.title' on line 30, col 18
        if _v is not None: write(_filter(_v, rawExpr=u'$now.title')) # from line 30, col 18.
        write(u'''</e2eventtitle>
\t\t\t<e2eventdescription>''')
        _v = VFFSL(SL,"now.shortdesc",True) # u'$now.shortdesc' on line 31, col 24
        if _v is not None: write(_filter(_v, rawExpr=u'$now.shortdesc')) # from line 31, col 24.
        write(u'''</e2eventdescription>
\t\t\t<e2eventstart>''')
        _v = VFFSL(SL,"now.begin_timestamp",True) # u'$now.begin_timestamp' on line 32, col 18
        if _v is not None: write(_filter(_v, rawExpr=u'$now.begin_timestamp')) # from line 32, col 18.
        write(u'''</e2eventstart>
\t\t\t<e2eventduration>''')
        _v = VFFSL(SL,"now.duration_sec",True) # u'$now.duration_sec' on line 33, col 21
        if _v is not None: write(_filter(_v, rawExpr=u'$now.duration_sec')) # from line 33, col 21.
        write(u'''</e2eventduration>
\t\t\t<e2eventremaining>''')
        _v = VFFSL(SL,"now.remaining",True) # u'$now.remaining' on line 34, col 22
        if _v is not None: write(_filter(_v, rawExpr=u'$now.remaining')) # from line 34, col 22.
        write(u'''</e2eventremaining>
\t\t\t<e2eventcurrenttime>''')
        _v = VFFSL(SL,"now.now_timestamp",True) # u'$now.now_timestamp' on line 35, col 24
        if _v is not None: write(_filter(_v, rawExpr=u'$now.now_timestamp')) # from line 35, col 24.
        write(u'''</e2eventcurrenttime>
\t\t\t<e2eventdescriptionextended>''')
        _v = VFFSL(SL,"now.longdesc",True) # u'$now.longdesc' on line 36, col 32
        if _v is not None: write(_filter(_v, rawExpr=u'$now.longdesc')) # from line 36, col 32.
        write(u'''</e2eventdescriptionextended>
\t\t</e2event>
\t\t<e2event>
\t\t\t<e2eventservicereference>''')
        _v = VFFSL(SL,"next.sref",True) # u'$next.sref' on line 39, col 29
        if _v is not None: write(_filter(_v, rawExpr=u'$next.sref')) # from line 39, col 29.
        write(u'''</e2eventservicereference>
\t\t\t<e2eventservicename>''')
        _v = VFFSL(SL,"next.sname",True) # u'$next.sname' on line 40, col 24
        if _v is not None: write(_filter(_v, rawExpr=u'$next.sname')) # from line 40, col 24.
        write(u'''</e2eventservicename>
\t\t\t<e2eventprovidername>''')
        _v = VFFSL(SL,"next.provider",True) # u'$next.provider' on line 41, col 25
        if _v is not None: write(_filter(_v, rawExpr=u'$next.provider')) # from line 41, col 25.
        write(u'''</e2eventprovidername>
\t\t\t<e2eventid>''')
        _v = VFFSL(SL,"next.id",True) # u'$next.id' on line 42, col 15
        if _v is not None: write(_filter(_v, rawExpr=u'$next.id')) # from line 42, col 15.
        write(u'''</e2eventid>
\t\t\t<e2eventname>''')
        _v = VFFSL(SL,"next.title",True) # u'$next.title' on line 43, col 17
        if _v is not None: write(_filter(_v, rawExpr=u'$next.title')) # from line 43, col 17.
        write(u'''</e2eventname>
\t\t\t<e2eventtitle>''')
        _v = VFFSL(SL,"next.title",True) # u'$next.title' on line 44, col 18
        if _v is not None: write(_filter(_v, rawExpr=u'$next.title')) # from line 44, col 18.
        write(u'''</e2eventtitle>
\t\t\t<e2eventdescription>''')
        _v = VFFSL(SL,"next.shortdesc",True) # u'$next.shortdesc' on line 45, col 24
        if _v is not None: write(_filter(_v, rawExpr=u'$next.shortdesc')) # from line 45, col 24.
        write(u'''</e2eventdescription>
\t\t\t<e2eventstart>''')
        _v = VFFSL(SL,"next.begin_timestamp",True) # u'$next.begin_timestamp' on line 46, col 18
        if _v is not None: write(_filter(_v, rawExpr=u'$next.begin_timestamp')) # from line 46, col 18.
        write(u'''</e2eventstart>
\t\t\t<e2eventduration>''')
        _v = VFFSL(SL,"next.duration_sec",True) # u'$next.duration_sec' on line 47, col 21
        if _v is not None: write(_filter(_v, rawExpr=u'$next.duration_sec')) # from line 47, col 21.
        write(u'''</e2eventduration>
\t\t\t<e2eventremaining>''')
        _v = VFFSL(SL,"next.remaining",True) # u'$next.remaining' on line 48, col 22
        if _v is not None: write(_filter(_v, rawExpr=u'$next.remaining')) # from line 48, col 22.
        write(u'''</e2eventremaining>
\t\t\t<e2eventcurrenttime>''')
        _v = VFFSL(SL,"next.now_timestamp",True) # u'$next.now_timestamp' on line 49, col 24
        if _v is not None: write(_filter(_v, rawExpr=u'$next.now_timestamp')) # from line 49, col 24.
        write(u'''</e2eventcurrenttime>
\t\t\t<e2eventdescriptionextended>''')
        _v = VFFSL(SL,"next.longdesc",True) # u'$next.longdesc' on line 50, col 32
        if _v is not None: write(_filter(_v, rawExpr=u'$next.longdesc')) # from line 50, col 32.
        write(u'''</e2eventdescriptionextended>
\t\t</e2event>
\t</e2eventlist>
</e2currentserviceinformation>
''')
        _filter = self._CHEETAH__currentFilter = _orig_filter_47255804
        
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

    _mainCheetahMethod_for_getcurrent= 'respond'

## END CLASS DEFINITION

if not hasattr(getcurrent, '_initCheetahAttributes'):
    templateAPIClass = getattr(getcurrent, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(getcurrent)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=getcurrent()).run()

