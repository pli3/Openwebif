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
__CHEETAH_genTime__ = 1364979191.948121
__CHEETAH_genTimestamp__ = 'Wed Apr  3 17:53:11 2013'
__CHEETAH_src__ = '/home/fermi/Work/Model/tmsingle/openpli3.0/build-tmsingle/tmp/work/mips32el-oe-linux/enigma2-plugin-extensions-openwebif-0.1+git1+279a2577c3bc6defebd4bf9e61a046dcf7f37c01-r0.72/git/plugin/controllers/views/main.tmpl'
__CHEETAH_srcLastModified__ = 'Wed Apr  3 17:10:17 2013'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class main(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(main, self).__init__(*args, **KWs)
        if not self._CHEETAH__instanceInitialized:
            cheetahKWArgs = {}
            allowedKWs = 'searchList namespaces filter filtersLib errorCatcher'.split()
            for k,v in KWs.items():
                if k in allowedKWs: cheetahKWArgs[k] = v
            self._initCheetahInstance(**cheetahKWArgs)
        

    def menu(self, title, name, content, **KWS):



        ## CHEETAH: generated from #def menu($title, $name, $content) at line 34, col 4.
        trans = KWS.get("trans")
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
        
        write(u'''\t\t\t<div id="leftmenu_main">\r
\t\t\t\t<div id="leftmenu_top">\r
\t\t\t\t\t''')
        _v = VFFSL(SL,"title",True) # u'$title' on line 37, col 6
        if _v is not None: write(_filter(_v, rawExpr=u'$title')) # from line 37, col 6.
        write(u'''\r
''')
        if VFFSL(SL,"name",True) in VFFSL(SL,"collapsed",True): # generated from line 38, col 6
            write(u'''\t\t\t\t\t<div id="leftmenu_expander_''')
            _v = VFFSL(SL,"name",True) # u'$name' on line 39, col 33
            if _v is not None: write(_filter(_v, rawExpr=u'$name')) # from line 39, col 33.
            write(u'''" class="leftmenu_icon leftmenu_icon_collapse" onclick="toggleMenu(\'''')
            _v = VFFSL(SL,"name",True) # u'$name' on line 39, col 106
            if _v is not None: write(_filter(_v, rawExpr=u'$name')) # from line 39, col 106.
            write(u'''\');"></div>\r
''')
        else: # generated from line 40, col 6
            write(u'''\t\t\t\t\t<div id="leftmenu_expander_''')
            _v = VFFSL(SL,"name",True) # u'$name' on line 41, col 33
            if _v is not None: write(_filter(_v, rawExpr=u'$name')) # from line 41, col 33.
            write(u'''" class="leftmenu_icon" onclick="toggleMenu(\'''')
            _v = VFFSL(SL,"name",True) # u'$name' on line 41, col 83
            if _v is not None: write(_filter(_v, rawExpr=u'$name')) # from line 41, col 83.
            write(u'''\');"></div>\r
''')
        write(u'''\t\t\t\t</div>\r
''')
        if VFFSL(SL,"name",True) in VFFSL(SL,"collapsed",True): # generated from line 44, col 5
            write(u'''\t\t\t\t<div id="leftmenu_container_''')
            _v = VFFSL(SL,"name",True) # u'$name' on line 45, col 33
            if _v is not None: write(_filter(_v, rawExpr=u'$name')) # from line 45, col 33.
            write(u'''" style="display: none;">\r
''')
        else: # generated from line 46, col 5
            write(u'''\t\t\t\t<div id="leftmenu_container_''')
            _v = VFFSL(SL,"name",True) # u'$name' on line 47, col 33
            if _v is not None: write(_filter(_v, rawExpr=u'$name')) # from line 47, col 33.
            write(u'''">\r
''')
        write(u'''\t\t\t\t''')
        _v = VFFSL(SL,"content",True) # u'$content' on line 49, col 5
        if _v is not None: write(_filter(_v, rawExpr=u'$content')) # from line 49, col 5.
        write(u'''\r
\t\t\t\t</div>\r
\t\t\t</div>\r
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def mainMenu(self, **KWS):



        ## CHEETAH: generated from #def mainMenu at line 54, col 4.
        trans = KWS.get("trans")
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
        
        write(u'''\t\t\t<ul>\r
\t\t\t\t<li><a href=\'#\' onclick="load_maincontent(\'ajax/tv\'); return false;">Television</a></li>\r
\t\t\t\t<li><a href=\'#\' onclick="load_maincontent(\'ajax/radio\'); return false;">Radio</a></li>\r
\t\t\t</ul>\r
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def volumeMenu(self, **KWS):



        ## CHEETAH: generated from #def volumeMenu at line 61, col 4.
        trans = KWS.get("trans")
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
        
        write(u'''\t\t\t<div class="volslider">\r
\t\t\t\t\t<p style="text-align:center; padding-bottom:8px;"> \r
\t\t\t\t\t\t<label for="amount">Volume:</label>\r
\t\t\t\t\t\t<input type="text" id="amount" style="border:0; color:#f6931f; font-weight:bold; width:40px;" />\r
\t\t\t\t\t</p>\r
\t\t\t\t<div id="slider" style="width:130px;"></div>\r
\t\t\t</div>\r
\t\t\t<div style="width:100%; text-align:center; padding-top:5px; padding-bottom:10px;"><img id="volimage" src="images/volume.png" title="" border="0"></div>\r
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def controlMenu(self, **KWS):



        ## CHEETAH: generated from #def controlMenu at line 72, col 4.
        trans = KWS.get("trans")
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
        
        write(u'''\t\t\t<ul>\r
\t\t\t\t<li><a href=\'#\' onclick="load_maincontent(\'ajax/powerstate\'); return false;">Power Control</a></li>\r
\t\t\t\t<li><a href=\'#\' onclick="load_maincontent(\'ajax/screenshot\'); return false;">Grab Screenshot</a></li>\r
\t\t\t\t<li><a href=\'#\' onclick="load_maincontent(\'ajax/message\'); return false;">Send a Message</a></li>\r
\t\t\t\t<li><a href=\'#\' onclick="load_maincontent(\'ajax/timers\'); return false;">Timers</a></li>\r
\t\t\t</ul>\r
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def infoMenu(self, **KWS):



        ## CHEETAH: generated from #def infoMenu at line 81, col 4.
        trans = KWS.get("trans")
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
        
        write(u'''\t\t\t<ul>\r
\t\t\t\t<li><a href="#" onclick="load_maincontent(\'ajax/boxinfo\'); return false">Box Info</a></li>\r
\t\t\t\t<li><a href="#" onclick="load_maincontent(\'ajax/about\'); return false">About</a></li>\r
\t\t\t</ul>\r
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def streamMenu(self, **KWS):



        ## CHEETAH: generated from #def streamMenu at line 88, col 4.
        trans = KWS.get("trans")
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
        
        write(u'''\t\t\t<ul>\r
\t\t\t\t<li><a href=\'#\' onclick="load_maincontent_spin(\'ajax/movies\'); return false;">Movies</a></li>\r
 <!--\t\t\t\t<li><a href=\'#\' onclick="load_maincontent(\'ajax/workinprogress\'); return false;">Web Tv</a></li> -->\r
''')
        if VFFSL(SL,"zapstream",True): # generated from line 92, col 5
            write(u'''\t\t\t\t<li><input type="checkbox" name="zapstream" checked="checked" />zap before Stream</li>\r
''')
        else: # generated from line 94, col 5
            write(u'''\t\t\t\t<li><input type="checkbox" name="zapstream" />zap before Stream</li>\r
''')
        write(u'''\t\t\t</ul>\r
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def searchMenu(self, **KWS):



        ## CHEETAH: generated from #def searchMenu at line 100, col 4.
        trans = KWS.get("trans")
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
        
        write(u'''\t\t\t<form action="" onSubmit="open_epg_search_pop(); return false;">\r
\t\t\t\t<div style="width:100%; text-align:center; padding-top:5px;"><input type="text" id="epgSearch" size="14" /></div>\r
\t\t\t\t<div style="width:100%; text-align:center;padding-top:5px; padding-bottom:7px;" class="epgsearch"><button>Search</button></div>\r
\t\t\t</form>\r
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def remoteMenu(self, **KWS):



        ## CHEETAH: generated from #def remoteMenu at line 107, col 4.
        trans = KWS.get("trans")
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
        
        write(u'''\t\t\t<div style="width:100%; text-align:center;">\r
\t\t\t\t<img src="images/remotes/ow_remote.png" width="135" height="183" usemap="#menuremote" border="0">\r
\t\t\t\t<map name="menuremote" >\r
\t\t\t\t\t<area shape="circle" coords="67,148,13" alt="ok" onclick="pressMenuRemote(\'352\');">\r
\t\t\t\t\t<area shape="circle" coords="68,173,9" alt="down" onclick="pressMenuRemote(\'108\');">\r
\t\t\t\t\t<area shape="circle" coords="44,148,9" alt="left" onclick="pressMenuRemote(\'105\');">\r
\t\t\t\t\t<area shape="circle" coords="92,147,9" alt="right" onclick="pressMenuRemote(\'106\');">\r
\t\t\t\t\t<area shape="circle" coords="68,126,8" alt="up" onclick="pressMenuRemote(\'103\');">\r
\t\t\t\t\t<area shape="circle" coords="117,163,10" alt="blue" onclick="pressMenuRemote(\'401\');">\r
\t\t\t\t\t<area shape="circle" coords="118,132,11" alt="yellow" onclick="pressMenuRemote(\'400\');">\r
\t\t\t\t\t<area shape="circle" coords="18,163,11" alt="green" onclick="pressMenuRemote(\'399\');">\r
\t\t\t\t\t<area shape="circle" coords="19,133,10" alt="red" onclick="pressMenuRemote(\'398\');">\r
\t\t\t\t\t<area shape="rect" coords="5,89,44,117" alt="menu" onclick="pressMenuRemote(\'139\');">\r
\t\t\t\t\t<area shape="rect" coords="90,89,128,117" alt="exit" onclick="pressMenuRemote(\'174\');">\r
\t\t\t\t\t<area shape="rect" coords="47,89,87,117" alt="0" onclick="pressMenuRemote(\'11\');">\r
\t\t\t\t\t<area shape="rect" coords="90,60,128,86" alt="9" onclick="pressMenuRemote(\'10\');">\r
\t\t\t\t\t<area shape="rect" coords="47,60,87,86" alt="8" onclick="pressMenuRemote(\'9\');">\r
\t\t\t\t\t<area shape="rect" coords="4,60,44,86" alt="7" onclick="pressMenuRemote(\'8\');">\r
\t\t\t\t\t<area shape="rect" coords="90,30,129,57" alt="6" onclick="pressMenuRemote(\'7\');">\r
\t\t\t\t\t<area shape="rect" coords="47,30,87,57" alt="5" onclick="pressMenuRemote(\'6\');">\r
\t\t\t\t\t<area shape="rect" coords="4,30,44,57" alt="4" onclick="pressMenuRemote(\'5\');">\r
\t\t\t\t\t<area shape="rect" coords="90,0,129,27" alt="3" onclick="pressMenuRemote(\'4\');">\r
\t\t\t\t\t<area shape="rect" coords="46,0,88,28" alt="2" onclick="pressMenuRemote(\'3\');">\r
\t\t\t\t\t<area shape="rect" coords="5,0,45,28" alt="1" onclick="pressMenuRemote(\'2\');">\r
\t\t\t\t</map>\r
\t\t\t\t<div id="help">\r
\t\t\t\t\t(shift + click for long pressure)\r
\t\t\t\t</div>\r
\t\t\t\t<ul>\r
''')
        if VFFSL(SL,"remotegrabscreenshot",True): # generated from line 137, col 6
            write(u'''\t\t\t\t\t<li><input type="checkbox" name="remotegrabscreen" checked="checked" />Grab screenshot</li>\r
''')
        else: # generated from line 139, col 6
            write(u'''\t\t\t\t\t<li><input type="checkbox" name="remotegrabscreen" />Grab screenshot</li>\r
''')
        write(u'''\t\t\t\t\t<li><a href="#" onclick="toggleFullRemote(); return false;">Show full remote</a></li>\r
\t\t\t\t</ul>\r
\t\t\t</div>\r
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def configMenu(self, **KWS):



        ## CHEETAH: generated from #def configMenu at line 147, col 4.
        trans = KWS.get("trans")
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
        
        write(u'''\t\t\t<ul>\r
''')
        for section in VFFSL(SL,"configsections",True): # generated from line 149, col 5
            write(u'''\t\t\t\t\t<li><a href=\'#\' onclick="load_maincontent(\'ajax/config?section=''')
            _v = VFFSL(SL,"section",True)["key"] # u'$section["key"]' on line 150, col 69
            if _v is not None: write(_filter(_v, rawExpr=u'$section["key"]')) # from line 150, col 69.
            write(u'''\'); return false;">''')
            _v = VFFSL(SL,"section",True)["description"] # u'$section["description"]' on line 150, col 103
            if _v is not None: write(_filter(_v, rawExpr=u'$section["description"]')) # from line 150, col 103.
            write(u'''</a></li>\r
''')
        write(u'''\t\t\t</ul>\r
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

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
        
        write(u'''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\r
<html xmlns="http://www.w3.org/1999/xhtml">\r
<head>\r
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\r
<link rel="shortcut icon" href="/images/favicon.png">\r
<link rel="stylesheet" type="text/css" href="/css/style.css" />\r
<link type="text/css" href="/css/jquery-ui-1.8.18.custom.css" rel="stylesheet" />\t\r
<script type="text/javascript" src="/js/jquery-1.6.2.min.js"></script>\r
<script type="text/javascript" src="/js/jquery-ui-1.8.18.custom.min.js"></script>\r
<script type="text/javascript" src="/js/openwebif.js"></script>\r
\r
<title>Open Webif</title>\r
</head>\r
\r
<body>\r
\t<div id="container">\r
\t\t<div id="header">\r
\t\t\t<h1><a href="/">Open<span class="off">Webif</span></a></h1>\r
\t\t\t<h2>Open Source Web Interface for Linux set-top box</h2>\r
\t\t</div>\r
\t\t\r
\t\t<div id="osd">\r
\t\t\tNothing playing.\r
\t\t</div>\r
\t\t<div id="osd_bottom">\r
\t\t\t\r
\t\t</div>\r
\t\t\r
\t\t<div id="dialog" title="Work in progress">\r
\t\t\t<p>Sorry, this function is not yet implemented.</p>\r
\t\t</div>\r
\t\t\r
\t\t<div id="leftmenu">\r
\t\t\r
\t\t\r
\r
\t\t\r
\t\t\r
\t\t\r
\t\t\t\r
\t\t\t\r
\t\t\r
\t\t\t<div id="menucontainer">\r
\t\t\t\t''')
        _v = VFFSL(SL,"menu",False)("Main", "main", VFFSL(SL,"mainMenu",True)) # u'$menu("Main", "main", $mainMenu)' on line 156, col 5
        if _v is not None: write(_filter(_v, rawExpr=u'$menu("Main", "main", $mainMenu)')) # from line 156, col 5.
        write(u'''\r
\t\t\t\t''')
        _v = VFFSL(SL,"menu",False)("Volume Control", "volume", VFFSL(SL,"volumeMenu",True)) # u'$menu("Volume Control", "volume", $volumeMenu)' on line 157, col 5
        if _v is not None: write(_filter(_v, rawExpr=u'$menu("Volume Control", "volume", $volumeMenu)')) # from line 157, col 5.
        write(u'''\r
\t\t\t\t''')
        _v = VFFSL(SL,"menu",False)("Box Control", "control", VFFSL(SL,"controlMenu",True)) # u'$menu("Box Control", "control", $controlMenu)' on line 158, col 5
        if _v is not None: write(_filter(_v, rawExpr=u'$menu("Box Control", "control", $controlMenu)')) # from line 158, col 5.
        write(u'''\r
\t\t\t\t''')
        _v = VFFSL(SL,"menu",False)("Remote", "remote", VFFSL(SL,"remoteMenu",True)) # u'$menu("Remote", "remote", $remoteMenu)' on line 159, col 5
        if _v is not None: write(_filter(_v, rawExpr=u'$menu("Remote", "remote", $remoteMenu)')) # from line 159, col 5.
        write(u'''\r
\t\t\t\t''')
        _v = VFFSL(SL,"menu",False)("Info", "info", VFFSL(SL,"infoMenu",True)) # u'$menu("Info", "info", $infoMenu)' on line 160, col 5
        if _v is not None: write(_filter(_v, rawExpr=u'$menu("Info", "info", $infoMenu)')) # from line 160, col 5.
        write(u'''\r
\t\t\t\t''')
        _v = VFFSL(SL,"menu",False)("Stream", "stream", VFFSL(SL,"streamMenu",True)) # u'$menu("Stream", "stream", $streamMenu)' on line 161, col 5
        if _v is not None: write(_filter(_v, rawExpr=u'$menu("Stream", "stream", $streamMenu)')) # from line 161, col 5.
        write(u'''\r
\t\t\t\t''')
        _v = VFFSL(SL,"menu",False)("Settings", "config", VFFSL(SL,"configMenu",True)) # u'$menu("Settings", "config", $configMenu)' on line 162, col 5
        if _v is not None: write(_filter(_v, rawExpr=u'$menu("Settings", "config", $configMenu)')) # from line 162, col 5.
        write(u'''\r
\t\t\t\t''')
        _v = VFFSL(SL,"menu",False)("Epg Search", "search", VFFSL(SL,"searchMenu",True)) # u'$menu("Epg Search", "search", $searchMenu)' on line 163, col 5
        if _v is not None: write(_filter(_v, rawExpr=u'$menu("Epg Search", "search", $searchMenu)')) # from line 163, col 5.
        write(u'''\r
\t\t\t</div>\r
\t\t\t<div id="remotecontainer" style="display: none;">\r
\t\t\t\t<div id="leftmenu_main">\r
\t\t\t\t\t<div id="leftmenu_top">Remote Control</div>\r
\t\t\t\t\t<div style="width:100%; text-align:center;">\r
\t\t\t\t\t\t<div id="remote_container" style="width:100%; text-align:center;"></div>\r
\t\t\t\t\t\t<script type="text/javascript">\r
\t\t\t\t\t\t\t$(document).ready(function() {\r
\t\t\t\t\t\t\t\t$("#remote_container").load("/static/remotes/''')
        _v = VFFSL(SL,"remote",True) # u'${remote}' on line 172, col 55
        if _v is not None: write(_filter(_v, rawExpr=u'${remote}')) # from line 172, col 55.
        write(u'''.html");\r
\t\t\t\t\t\t\t});\r
\t\t\t\t\t\t</script>\r
\t\t\t\t\t\t<div id="help">\r
\t\t\t\t\t\t\t(shift + click for long pressure)\r
\t\t\t\t\t\t</div>\r
\t\t\t\t\t\t<ul>\r
''')
        if VFFSL(SL,"remotegrabscreenshot",True): # generated from line 179, col 8
            write(u'''\t\t\t\t\t\t\t<li><input type="checkbox" name="remotegrabscreen" checked="checked" />Grab screenshot</li>\r
''')
        else: # generated from line 181, col 8
            write(u'''\t\t\t\t\t\t\t<li><input type="checkbox" name="remotegrabscreen" />Grab screenshot</li>\r
''')
        write(u'''\t\t\t\t\t\t\t<li><a href="#" onclick="toggleFullRemote(); return false;" class="leftmenu_remotelink">Hide full remote</a></li>\r
\t\t\t\t\t\t</ul>\r
\t\t\t\t\t</div>\r
\t\t\t\t</div>\r
\t\t\t</div>\r
\t\t</div>\r
\t\t\r
\t\t<div id="content">\r
\t\t\t<div id="content_container">\r
\t\t\t''')
        _v = VFFSL(SL,"content",True) # u'$content' on line 193, col 4
        if _v is not None: write(_filter(_v, rawExpr=u'$content')) # from line 193, col 4.
        write(u'''\r
\t\t\t</div>\r
\t\t\t<div id="footer"><h3>&nbsp;&nbsp;<a href="https://github.com/E2OpenPlugins">E2OpenPlugins</a> | <a href="http://www.vuplus-community.net">Black Hole</a> | <a href="http://openpli.org">OpenPli</a> | <a href="http://forum.sifteam.eu">Sif</a> | <a href="http://www.vuplus-support.org">Vti</a></h3></div>\r
\t\t</div>\r
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

    _mainCheetahMethod_for_main= 'respond'

## END CLASS DEFINITION

if not hasattr(main, '_initCheetahAttributes'):
    templateAPIClass = getattr(main, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(main)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=main()).run()

