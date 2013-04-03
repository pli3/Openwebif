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
import datetime

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '2.4.4'
__CHEETAH_versionTuple__ = (2, 4, 4, 'development', 0)
__CHEETAH_genTime__ = 1364979193.84299
__CHEETAH_genTimestamp__ = 'Wed Apr  3 17:53:13 2013'
__CHEETAH_src__ = '/home/fermi/Work/Model/tmsingle/openpli3.0/build-tmsingle/tmp/work/mips32el-oe-linux/enigma2-plugin-extensions-openwebif-0.1+git1+279a2577c3bc6defebd4bf9e61a046dcf7f37c01-r0.72/git/plugin/controllers/views/mobile/timerlist.tmpl'
__CHEETAH_srcLastModified__ = 'Wed Apr  3 17:10:17 2013'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class timerlist(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(timerlist, self).__init__(*args, **KWs)
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
        
        write(u'''<html>\r
 <head>\r
\t<title>OpenWebif</title>\r
\t<meta name="viewport" content="user-scalable=no, width=device-width"/>\r
\t<meta name="apple-mobile-web-app-capable" content="yes" />\r
\t<link rel="stylesheet" type="text/css" href="/css/jquery.mobile-1.0.min.css" media="screen"/>\r
\t<link rel="stylesheet" type="text/css" href="/css/iphone.css" media="screen"/>\r
\t<script src="/js/jquery-1.6.2.min.js"></script>\r
\t<script src="/js/jquery.mobile-1.0.min.js"></script>\r
 </head>\r
 <body> \r
\t<div data-role="page">\r
\r
\t\t<div id="header">\r
\t\t\t<div class="button" onClick="history.back()">Back</div>\r
\t\t\t<div class="button-bold">+</div>\r
\t\t\t<h1>OpenWebif</h1>\r
\t\t</div>\r
\r
\t\t<div id="contentContainer">\r
\t\t\t<ul data-role="listview" data-inset="true" data-theme="d">\r
\t\t\t\t<li data-role="list-divider" role="heading" data-theme="b">Timerlist</li>\r
''')
        for timer in VFFSL(SL,"timers",True): # generated from line 24, col 5
            duration = VFFSL(SL,"timer.duration",True)/60
            starttime = datetime.datetime.fromtimestamp(VFFSL(SL,"timer.begin",True)).strftime("%d.%m.%Y")
            endtime = datetime.datetime.fromtimestamp(VFFSL(SL,"timer.end",True)).strftime("%d.%m.%Y")
            write(u'''\t\t\t\t<li>\r
\t\t\t\t''')
            _v = VFFSL(SL,"timer.name",True) # u'$timer.name' on line 29, col 5
            if _v is not None: write(_filter(_v, rawExpr=u'$timer.name')) # from line 29, col 5.
            write(u''' (''')
            _v = VFFSL(SL,"timer.servicename",True) # u'$timer.servicename' on line 29, col 18
            if _v is not None: write(_filter(_v, rawExpr=u'$timer.servicename')) # from line 29, col 18.
            write(u''')<br />\r
\t\t\t\t''')
            _v = VFFSL(SL,"starttime",True) # u'$starttime' on line 30, col 5
            if _v is not None: write(_filter(_v, rawExpr=u'$starttime')) # from line 30, col 5.
            write(u''' - ''')
            _v = VFFSL(SL,"endtime",True) # u'$endtime' on line 30, col 18
            if _v is not None: write(_filter(_v, rawExpr=u'$endtime')) # from line 30, col 18.
            write(u''' (''')
            _v = VFFSL(SL,"duration",True) # u'$duration' on line 30, col 28
            if _v is not None: write(_filter(_v, rawExpr=u'$duration')) # from line 30, col 28.
            write(u''' min)\r
\t\t\t\t</li>\r
''')
        write(u'''\t\t\t</ul>\r
\t\t</div>\r
\r
\t\t<div id="footer">\r
\t\t\t<p>OpenWebif Mobile</p>\r
\t\t</div>\r
\t\t\r
\t</div>\r
 </body>\r
</html>\r
      ''')
        
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

    _mainCheetahMethod_for_timerlist= 'respond'

## END CLASS DEFINITION

if not hasattr(timerlist, '_initCheetahAttributes'):
    templateAPIClass = getattr(timerlist, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(timerlist)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=timerlist()).run()

