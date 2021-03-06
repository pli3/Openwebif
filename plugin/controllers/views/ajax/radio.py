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
__CHEETAH_genTime__ = 1364979192.815969
__CHEETAH_genTimestamp__ = 'Wed Apr  3 17:53:12 2013'
__CHEETAH_src__ = '/home/fermi/Work/Model/tmsingle/openpli3.0/build-tmsingle/tmp/work/mips32el-oe-linux/enigma2-plugin-extensions-openwebif-0.1+git1+279a2577c3bc6defebd4bf9e61a046dcf7f37c01-r0.72/git/plugin/controllers/views/ajax/radio.tmpl'
__CHEETAH_srcLastModified__ = 'Wed Apr  3 17:10:17 2013'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class radio(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(radio, self).__init__(*args, **KWs)
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
        
        write(u'''<div id="content_main">
\t<div id="tvcontentmain">
\t<div id="toolbar-header">
\t\t<span id="toolbar">
\t\t\t<span id="tvbutton">
\t\t\t\t<input type="radio" id="radiobutton0" name="radiobutton" checked="checked" /><label for="radiobutton0">Bouquets</label>
\t\t\t\t<input type="radio" id="radiobutton1" name="radiobutton" /><label for="radiobutton1">Providers</label>
\t\t\t\t<input type="radio" id="radiobutton2" name="radiobutton" /><label for="radiobutton2">Satellites</label>
\t\t\t\t<input type="radio" id="radiobutton3" name="radiobutton" /><label for="radiobutton3">All Channels</label>
\t\t\t</span>
\t\t</span>
\t</div>
\t
\t<div id="tvcontent"></div>
\t</div>
</div>

<script type="text/javascript">
\t$(\'#radiobutton0\').click(function(){
\t\t$("#tvcontent").html(loadspinner).load("ajax/bouquets?stype=radio");
\t});
\t$(\'#radiobutton1\').click(function(){
\t\t$("#tvcontent").html(loadspinner).load("ajax/providers?stype=radio");
\t});
\t$(\'#radiobutton2\').click(function(){
\t\t$("#tvcontent").load("ajax/satellites?stype=radio");
\t});
\t$(\'#radiobutton3\').click(function(){
\t\t$("#tvcontent").html(loadspinner).load("ajax/channels?stype=radio");
\t});
\t
\t$( "#tvbutton" ).buttonset();
\t
\t$(document).ready(function() {
\t\t$("#tvcontent").load("ajax/bouquets?stype=radio");
\t});
</script>

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

    _mainCheetahMethod_for_radio= 'respond'

## END CLASS DEFINITION

if not hasattr(radio, '_initCheetahAttributes'):
    templateAPIClass = getattr(radio, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(radio)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=radio()).run()


