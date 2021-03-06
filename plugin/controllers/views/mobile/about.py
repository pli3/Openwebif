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
__CHEETAH_genTime__ = 1364979193.796381
__CHEETAH_genTimestamp__ = 'Wed Apr  3 17:53:13 2013'
__CHEETAH_src__ = '/home/fermi/Work/Model/tmsingle/openpli3.0/build-tmsingle/tmp/work/mips32el-oe-linux/enigma2-plugin-extensions-openwebif-0.1+git1+279a2577c3bc6defebd4bf9e61a046dcf7f37c01-r0.72/git/plugin/controllers/views/mobile/about.tmpl'
__CHEETAH_srcLastModified__ = 'Wed Apr  3 17:10:17 2013'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class about(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(about, self).__init__(*args, **KWs)
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
\t<meta name="viewport" content="user-scalable=no, width=device-width"/>\r
\t<meta name="apple-mobile-web-app-capable" content="yes" />\r
\t<link rel="stylesheet" href="http://code.jquery.com/mobile/1.0/jquery.mobile-1.0.min.css" />\r
\t<link rel="stylesheet" type="text/css" href="/css/iphone.css" media="screen"/>\r
\t<script src="/js/jquery-1.6.2.min.js"></script>\r
\t<script src="/js/jquery.mobile-1.0.min.js"></script>\r
\t<script src="/js/openwebif.mobile.js"></script>\r
 </head>\r
 <body> \r
\t<div data-role="page">\r
\r
\t\t<div id="header">\r
\t\t\t<div class="button" onClick="history.back()">Back</div>\r
\t\t\t<h1>OpenWebif</h1>\r
\t\t</div>\r
\r
\t\t<div id="contentContainer">\r
\t\t\t<div id="mainContent" style="text-align: center;">
\t\t\t\t<h3>OpenWebif</h3>
\t\t\t\t<h3>Open Source Web Interface for Linux Set-Top Box</h3>
\t\t\t\t<h3>Site and sources: <a href="https://github.com/E2OpenPlugins/e2openplugin-OpenWebif">Github</a></h3>
\t\t\t\t<hr>\t\t\t
\t\t\t\t<br>
\t\t\t\t<h1>Authors</h1>
\t\t\t\t<div class="info">
\t\t\t\t\tmeo aka bacicciosat<br>\t
\t\t\t\t\tskaman<br>
\t\t\t\t\tHomey-GER<br>
\t\t\t\t</div>
\t\t\t\t<hr>
\t\t\t\t<br>\t
\t\t\t\t<h1>Javascript Libraries</h1>\t\t\t\t\t\t
\t\t\t\t<div class="info">
\t\t\t\t\t<a href="http://jqueryui.com/">jQuery UI</a><br>\r
\t\t\t\t\t<a href="http://jquerymobile.com/">jQuery Mobile</a>
\t\t\t\t</div>
\t\t\t\t<hr>
\t\t\t\t<br>\t
\t\t\t\t<h1>Template Engine</h1>\t\t\t\t\t\t
\t\t\t\t<div class="info">
\t\t\t\t\t<a href="http://www.cheetahtemplate.org/">Cheetah</a>
\t\t\t\t</div>
\t\t\t\t<hr>
\t\t\t\t<br>\t\t\t
\t\t\t\t<h1>LICENSE</h1>
\t\t\t\tAll Files of this Software are open source software; you can redistribute it and/or modify it under the terms of the GNU General Public License version 2 as published by the Free Software Foundation.
\t\t\t</div>\r
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

    _mainCheetahMethod_for_about= 'respond'

## END CLASS DEFINITION

if not hasattr(about, '_initCheetahAttributes'):
    templateAPIClass = getattr(about, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(about)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=about()).run()


