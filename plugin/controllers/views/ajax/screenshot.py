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
__CHEETAH_genTime__ = 1364979193.574976
__CHEETAH_genTimestamp__ = 'Wed Apr  3 17:53:13 2013'
__CHEETAH_src__ = '/home/fermi/Work/Model/tmsingle/openpli3.0/build-tmsingle/tmp/work/mips32el-oe-linux/enigma2-plugin-extensions-openwebif-0.1+git1+279a2577c3bc6defebd4bf9e61a046dcf7f37c01-r0.72/git/plugin/controllers/views/ajax/screenshot.tmpl'
__CHEETAH_srcLastModified__ = 'Wed Apr  3 17:10:17 2013'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class screenshot(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(screenshot, self).__init__(*args, **KWs)
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
        
        write(u'''<div id="content_main" style="min-height: 533px;">
\t<div id="info">
\t\t<h3>Screenshot</h3>

\t\t<div id="toolbar-header">
\t\t\t<span id="toolbar">
\t\t\t\t<span id="screenshotbutton">
\t\t\t\t\t<input type="radio" id="screenshotbutton0" name="screenshotbutton" onclick="grabScreenshot(\'all\'); return false" checked="checked" /><label for="screenshotbutton0">Screenshot (All)</label>
\t\t\t\t\t<input type="radio" id="screenshotbutton1" name="screenshotbutton" onclick="grabScreenshot(\'video\'); return false" /><label for="screenshotbutton1">Screenshot (Video)</label>
\t\t\t\t\t<input type="radio" id="screenshotbutton2" name="screenshotbutton" onclick="grabScreenshot(\'osd\'); return false" /><label for="screenshotbutton2">Screenshot (OSD)</label>
\t\t\t\t</span>
\t\t\t</span>
\t\t</div>
\t

\t
\t\t<div class="screenshotContainer">
\t\t\t<img id="screenshotspinner" src="/images/spinner.gif" border="0" alt="Loading ..." style="display: none;">
\t\t\t<img id="screenshotimage" src="/images/spinner.gif" alt="">
\t\t</div>
\t\t
\t\t<div id="screenShotRefresh" style="margin-top: 15px; margin-left: auto; margin-right: auto; width: 700px; text-align: center;">
\t\t\t<a href="#" onclick="grabScreenshot(\'auto\'); return false;">Refresh</a>
\t\t\t-
\t\t\t<input type="checkbox" id="screenshotRefreshHD" value="0">
\t\t\tHigh Resolution -
\t\t\t<input type="checkbox" id="screenshotRefreshStatus" value="0">
\t\t\tRefresh automatically every
\t\t\t<input type="text" size="1" id="screenshotRefreshInterval" value="30">
\t\t\tseconds
\t\t</div>
\t</div>
</div>

<script type="text/javascript">
\t$(\'#screenshotbutton\').buttonset();
\t$(\'#screenshotRefreshStatus\').attr(\'checked\', false);
\t$(\'#screenshotRefreshInterval\').val(30);
\t
\tvar screenshotInterval = false;
\t
\t$(\'#screenshotRefreshInterval\').change(function() {
\t\tif ($(\'#screenshotRefreshStatus\').is(\':checked\')) {
\t\t\tclearInterval(screenshotInterval); 
\t\t\tscreenshotInterval = 
\t\t\t\tsetInterval("grabScreenshot(\'auto\')", 
\t\t\t\t\t(parseInt(jQuery(\'#screenshotRefreshInterval\').val())+1)*1000);
\t\t}
\t});
\t
\t$(\'#screenshotRefreshStatus\').change(function() {
\t\tif ($(\'#screenshotRefreshStatus\').is(\':checked\')) {
\t\t\tscreenshotInterval = 
\t\t\t\tsetInterval("grabScreenshot(\'auto\')", 
\t\t\t\t\t(parseInt(jQuery(\'#screenshotRefreshInterval\').val())+1)*1000);
\t\t} else {
\t\t\tclearInterval(screenshotInterval); 
\t\t}
\t});

\t$(\'#screenshotRefreshHD\').change(function() {
\t\tgrabScreenshot(\'auto\');
\t});

\t$(document).ready(function() {
\t\tscreenshotMode = \'all\'; // reset on page reload
\t\tgrabScreenshot(screenshotMode);
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

    _mainCheetahMethod_for_screenshot= 'respond'

## END CLASS DEFINITION

if not hasattr(screenshot, '_initCheetahAttributes'):
    templateAPIClass = getattr(screenshot, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(screenshot)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=screenshot()).run()

