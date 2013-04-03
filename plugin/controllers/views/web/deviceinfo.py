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
__CHEETAH_genTime__ = 1364979192.551085
__CHEETAH_genTimestamp__ = 'Wed Apr  3 17:53:12 2013'
__CHEETAH_src__ = '/home/fermi/Work/Model/tmsingle/openpli3.0/build-tmsingle/tmp/work/mips32el-oe-linux/enigma2-plugin-extensions-openwebif-0.1+git1+279a2577c3bc6defebd4bf9e61a046dcf7f37c01-r0.72/git/plugin/controllers/views/web/deviceinfo.tmpl'
__CHEETAH_srcLastModified__ = 'Wed Apr  3 17:10:17 2013'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class deviceinfo(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(deviceinfo, self).__init__(*args, **KWs)
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
        
        _orig_filter_63410281 = _filter
        filterName = u'WebSafe'
        if self._CHEETAH__filters.has_key("WebSafe"):
            _filter = self._CHEETAH__currentFilter = self._CHEETAH__filters[filterName]
        else:
            _filter = self._CHEETAH__currentFilter = \
			self._CHEETAH__filters[filterName] = getattr(self._CHEETAH__filtersLib, filterName)(self).filter
        write(u'''<?xml version="1.0" encoding="UTF-8"?>
<e2deviceinfo>
\t<e2enigmaversion>''')
        _v = VFFSL(SL,"enigmaver",True) # u'$enigmaver' on line 4, col 19
        if _v is not None: write(_filter(_v, rawExpr=u'$enigmaver')) # from line 4, col 19.
        write(u'''</e2enigmaversion>
\t<e2imageversion>''')
        _v = VFFSL(SL,"imagever",True) # u'$imagever' on line 5, col 18
        if _v is not None: write(_filter(_v, rawExpr=u'$imagever')) # from line 5, col 18.
        write(u'''</e2imageversion>
\t<e2webifversion>''')
        _v = VFFSL(SL,"webifver",True) # u'$webifver' on line 6, col 18
        if _v is not None: write(_filter(_v, rawExpr=u'$webifver')) # from line 6, col 18.
        write(u'''</e2webifversion>
\t<e2fpversion>''')
        _v = VFFSL(SL,"str",False)(VFFSL(SL,"fp_version",True)) # u'$str($fp_version)' on line 7, col 15
        if _v is not None: write(_filter(_v, rawExpr=u'$str($fp_version)')) # from line 7, col 15.
        write(u'''</e2fpversion>
\t<e2devicename>''')
        _v = VFFSL(SL,"model",True) # u'$model' on line 8, col 16
        if _v is not None: write(_filter(_v, rawExpr=u'$model')) # from line 8, col 16.
        write(u'''</e2devicename>
\t<e2frontends>
''')
        for tuner in VFFSL(SL,"tuners",True): # generated from line 10, col 3
            write(u'''\t\t<e2frontend>
\t\t\t<e2name>''')
            _v = VFFSL(SL,"tuner.name",True) # u'$tuner.name' on line 12, col 12
            if _v is not None: write(_filter(_v, rawExpr=u'$tuner.name')) # from line 12, col 12.
            write(u'''</e2name>
\t\t\t<e2model>''')
            _v = VFFSL(SL,"tuner.type",True) # u'$tuner.type' on line 13, col 13
            if _v is not None: write(_filter(_v, rawExpr=u'$tuner.type')) # from line 13, col 13.
            write(u'''</e2model>
\t\t</e2frontend>
''')
        write(u'''\t</e2frontends>
\t<e2network>
''')
        for iface in VFFSL(SL,"ifaces",True): # generated from line 18, col 3
            write(u'''\t\t<e2interface>
\t\t\t<e2name>''')
            _v = VFFSL(SL,"iface.name",True) # u'$iface.name' on line 20, col 12
            if _v is not None: write(_filter(_v, rawExpr=u'$iface.name')) # from line 20, col 12.
            write(u'''</e2name>
\t\t\t<e2mac>''')
            _v = VFFSL(SL,"iface.mac",True) # u'$iface.mac' on line 21, col 11
            if _v is not None: write(_filter(_v, rawExpr=u'$iface.mac')) # from line 21, col 11.
            write(u'''</e2mac>
\t\t\t<e2dhcp>''')
            _v = VFFSL(SL,"iface.dhcp",True) # u'$iface.dhcp' on line 22, col 12
            if _v is not None: write(_filter(_v, rawExpr=u'$iface.dhcp')) # from line 22, col 12.
            write(u'''</e2dhcp>
\t\t\t<e2ip>''')
            _v = VFFSL(SL,"iface.ip",True) # u'$iface.ip' on line 23, col 10
            if _v is not None: write(_filter(_v, rawExpr=u'$iface.ip')) # from line 23, col 10.
            write(u'''</e2ip>
\t\t\t<e2gateway>''')
            _v = VFFSL(SL,"iface.gw",True) # u'$iface.gw' on line 24, col 15
            if _v is not None: write(_filter(_v, rawExpr=u'$iface.gw')) # from line 24, col 15.
            write(u'''</e2gateway>
\t\t\t<e2netmask>''')
            _v = VFFSL(SL,"iface.mask",True) # u'$iface.mask' on line 25, col 15
            if _v is not None: write(_filter(_v, rawExpr=u'$iface.mask')) # from line 25, col 15.
            write(u'''</e2netmask>
\t\t</e2interface>
''')
        write(u'''\t</e2network>
\t<e2hdds>
''')
        for hd in VFFSL(SL,"hdd",True): # generated from line 30, col 3
            write(u'''\t\t<e2hdd>
\t\t\t<e2model>''')
            _v = VFFSL(SL,"hd.model",True) # u'$hd.model' on line 32, col 13
            if _v is not None: write(_filter(_v, rawExpr=u'$hd.model')) # from line 32, col 13.
            write(u'''</e2model>
\t\t\t<e2capacity>''')
            _v = VFFSL(SL,"hd.capacity",True) # u'$hd.capacity' on line 33, col 16
            if _v is not None: write(_filter(_v, rawExpr=u'$hd.capacity')) # from line 33, col 16.
            write(u'''</e2capacity>
\t\t\t<e2free>''')
            _v = VFFSL(SL,"hd.free",True) # u'$hd.free' on line 34, col 12
            if _v is not None: write(_filter(_v, rawExpr=u'$hd.free')) # from line 34, col 12.
            write(u'''</e2free>
\t\t</e2hdd>
''')
        write(u'''\t</e2hdds>
</e2deviceinfo>
''')
        _filter = self._CHEETAH__currentFilter = _orig_filter_63410281
        
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

    _mainCheetahMethod_for_deviceinfo= 'respond'

## END CLASS DEFINITION

if not hasattr(deviceinfo, '_initCheetahAttributes'):
    templateAPIClass = getattr(deviceinfo, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(deviceinfo)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=deviceinfo()).run()


