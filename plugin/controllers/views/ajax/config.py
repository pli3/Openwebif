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
__CHEETAH_genTime__ = 1364979193.483411
__CHEETAH_genTimestamp__ = 'Wed Apr  3 17:53:13 2013'
__CHEETAH_src__ = '/home/fermi/Work/Model/tmsingle/openpli3.0/build-tmsingle/tmp/work/mips32el-oe-linux/enigma2-plugin-extensions-openwebif-0.1+git1+279a2577c3bc6defebd4bf9e61a046dcf7f37c01-r0.72/git/plugin/controllers/views/ajax/config.tmpl'
__CHEETAH_srcLastModified__ = 'Wed Apr  3 17:10:17 2013'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class config(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(config, self).__init__(*args, **KWs)
        if not self._CHEETAH__instanceInitialized:
            cheetahKWArgs = {}
            allowedKWs = 'searchList namespaces filter filtersLib errorCatcher'.split()
            for k,v in KWs.items():
                if k in allowedKWs: cheetahKWArgs[k] = v
            self._initCheetahInstance(**cheetahKWArgs)
        

    def select(self, config, **KWS):



        ## CHEETAH: generated from #def select($config) at line 1, col 1.
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
        
        write(u'''<tr>
<td>''')
        _v = VFFSL(SL,"config.description",True) # u'$config.description' on line 3, col 5
        if _v is not None: write(_filter(_v, rawExpr=u'$config.description')) # from line 3, col 5.
        write(u'''</td>
<td>
\t<select id="''')
        _v = VFFSL(SL,"config.path",True) # u'$config.path' on line 5, col 14
        if _v is not None: write(_filter(_v, rawExpr=u'$config.path')) # from line 5, col 14.
        write(u'''" onchange="saveConfig(\'''')
        _v = VFFSL(SL,"config.path",True) # u'$config.path' on line 5, col 50
        if _v is not None: write(_filter(_v, rawExpr=u'$config.path')) # from line 5, col 50.
        write(u'''\', this.value);">
''')
        for choice in VFFSL(SL,"config.data.choices",True): # generated from line 6, col 3
            if VFFSL(SL,"config.data.current",True) == VFFSL(SL,"choice",True)[0]: # generated from line 7, col 4
                write(u'''\t\t\t\t<option value="''')
                _v = VFFSL(SL,"choice",True)[0] # u'$choice[0]' on line 8, col 20
                if _v is not None: write(_filter(_v, rawExpr=u'$choice[0]')) # from line 8, col 20.
                write(u'''" selected="true">''')
                _v = VFFSL(SL,"choice",True)[1] # u'$choice[1]' on line 8, col 48
                if _v is not None: write(_filter(_v, rawExpr=u'$choice[1]')) # from line 8, col 48.
                write(u'''</option>
''')
            else: # generated from line 9, col 4
                write(u'''\t\t\t\t<option value="''')
                _v = VFFSL(SL,"choice",True)[0] # u'$choice[0]' on line 10, col 20
                if _v is not None: write(_filter(_v, rawExpr=u'$choice[0]')) # from line 10, col 20.
                write(u'''">''')
                _v = VFFSL(SL,"choice",True)[1] # u'$choice[1]' on line 10, col 32
                if _v is not None: write(_filter(_v, rawExpr=u'$choice[1]')) # from line 10, col 32.
                write(u'''</option>
''')
        write(u'''\t</select>
</td>
</tr>
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def checkbox(self, config, **KWS):



        ## CHEETAH: generated from #def checkbox($config) at line 18, col 1.
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
        
        write(u'''<tr>
<td>''')
        _v = VFFSL(SL,"config.description",True) # u'$config.description' on line 20, col 5
        if _v is not None: write(_filter(_v, rawExpr=u'$config.description')) # from line 20, col 5.
        write(u'''</td>
<td>
''')
        if VFFSL(SL,"config.data.current",True): # generated from line 22, col 2
            write(u'''\t\t<input type="checkbox" id="''')
            _v = VFFSL(SL,"config.path",True) # u'$config.path' on line 23, col 30
            if _v is not None: write(_filter(_v, rawExpr=u'$config.path')) # from line 23, col 30.
            write(u'''" checked="true" onclick="saveConfig(\'''')
            _v = VFFSL(SL,"config.path",True) # u'$config.path' on line 23, col 80
            if _v is not None: write(_filter(_v, rawExpr=u'$config.path')) # from line 23, col 80.
            write(u'''\', this.checked);" />
''')
        else: # generated from line 24, col 2
            write(u'''\t\t<input type="checkbox" id="''')
            _v = VFFSL(SL,"config.path",True) # u'$config.path' on line 25, col 30
            if _v is not None: write(_filter(_v, rawExpr=u'$config.path')) # from line 25, col 30.
            write(u'''" onclick="saveConfig(\'''')
            _v = VFFSL(SL,"config.path",True) # u'$config.path' on line 25, col 65
            if _v is not None: write(_filter(_v, rawExpr=u'$config.path')) # from line 25, col 65.
            write(u'''\', this.checked);" />
''')
        write(u'''</td>
</tr>
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def multicheckbox(self, config, **KWS):



        ## CHEETAH: generated from #def multicheckbox($config) at line 31, col 1.
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
        
        write(u'''<tr>
<td>''')
        _v = VFFSL(SL,"config.description",True) # u'$config.description' on line 33, col 5
        if _v is not None: write(_filter(_v, rawExpr=u'$config.description')) # from line 33, col 5.
        write(u'''</td>
<td>
''')
        for choice in VFFSL(SL,"config.data.choices",True): # generated from line 35, col 2
            if VFFSL(SL,"choice",True) in VFFSL(SL,"config.data.current",True): # generated from line 36, col 3
                write(u'''\t\t\t<input type="checkbox" id="''')
                _v = VFFSL(SL,"config.path",True) # u'${config.path}' on line 37, col 31
                if _v is not None: write(_filter(_v, rawExpr=u'${config.path}')) # from line 37, col 31.
                write(u'''_''')
                _v = VFFSL(SL,"choice",True) # u'${choice}' on line 37, col 46
                if _v is not None: write(_filter(_v, rawExpr=u'${choice}')) # from line 37, col 46.
                write(u'''" checked="true" onclick="saveConfig(\'''')
                _v = VFFSL(SL,"config.path",True) # u'$config.path' on line 37, col 93
                if _v is not None: write(_filter(_v, rawExpr=u'$config.path')) # from line 37, col 93.
                write(u"""', """)
                _v = VFFSL(SL,"choice",True) # u'$choice' on line 37, col 108
                if _v is not None: write(_filter(_v, rawExpr=u'$choice')) # from line 37, col 108.
                write(u''');" />
''')
            else: # generated from line 38, col 3
                write(u'''\t\t\t<input type="checkbox" id="''')
                _v = VFFSL(SL,"config.path",True) # u'${config.path}' on line 39, col 31
                if _v is not None: write(_filter(_v, rawExpr=u'${config.path}')) # from line 39, col 31.
                write(u'''_''')
                _v = VFFSL(SL,"choice",True) # u'${choice}' on line 39, col 46
                if _v is not None: write(_filter(_v, rawExpr=u'${choice}')) # from line 39, col 46.
                write(u'''" onclick="saveConfig(\'''')
                _v = VFFSL(SL,"config.path",True) # u'$config.path' on line 39, col 78
                if _v is not None: write(_filter(_v, rawExpr=u'$config.path')) # from line 39, col 78.
                write(u"""', """)
                _v = VFFSL(SL,"choice",True) # u'$choice' on line 39, col 93
                if _v is not None: write(_filter(_v, rawExpr=u'$choice')) # from line 39, col 93.
                write(u''');" />
''')
            write(u'''\t\t''')
            _v = VFFSL(SL,"choice",True) # u'$choice' on line 41, col 3
            if _v is not None: write(_filter(_v, rawExpr=u'$choice')) # from line 41, col 3.
            write(u'''
''')
        write(u'''</td>
</tr>
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def number(self, config, **KWS):



        ## CHEETAH: generated from #def number($config) at line 47, col 1.
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
        
        write(u'''<tr>
<td>''')
        _v = VFFSL(SL,"config.description",True) # u'$config.description' on line 49, col 5
        if _v is not None: write(_filter(_v, rawExpr=u'$config.description')) # from line 49, col 5.
        write(u'''</td>
<td>
\t<input type="text" id="''')
        _v = VFFSL(SL,"config.path",True) # u'${config.path}' on line 51, col 25
        if _v is not None: write(_filter(_v, rawExpr=u'${config.path}')) # from line 51, col 25.
        write(u'''" value="''')
        _v = VFFSL(SL,"config.data.current",True) # u'$config.data.current' on line 51, col 48
        if _v is not None: write(_filter(_v, rawExpr=u'$config.data.current')) # from line 51, col 48.
        write(u'''" onkeydown="numberTextboxKeydownFilter(event);" onchange="saveConfig(\'''')
        _v = VFFSL(SL,"config.path",True) # u'$config.path' on line 51, col 139
        if _v is not None: write(_filter(_v, rawExpr=u'$config.path')) # from line 51, col 139.
        write(u'''\', this.value);">
</td>
</tr>
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
        
        write(u'''



<div id="content_main">
\t<h3>''')
        _v = VFFSL(SL,"title",True) # u'$title' on line 57, col 6
        if _v is not None: write(_filter(_v, rawExpr=u'$title')) # from line 57, col 6.
        write(u'''</h3>
\t<hr />
\t<table id="configuration">
''')
        for config in VFFSL(SL,"configs",True): # generated from line 60, col 3
            if VFFSL(SL,"config.data.type",True) == "select": # generated from line 61, col 4
                write(u'''\t\t\t\t''')
                _v = VFFSL(SL,"select",False)(VFFSL(SL,"config",True)) # u'$select($config)' on line 62, col 5
                if _v is not None: write(_filter(_v, rawExpr=u'$select($config)')) # from line 62, col 5.
                write(u'''
''')
            elif VFFSL(SL,"config.data.type",True) == "checkbox": # generated from line 63, col 4
                write(u'''\t\t\t\t''')
                _v = VFFSL(SL,"checkbox",False)(VFFSL(SL,"config",True)) # u'$checkbox($config)' on line 64, col 5
                if _v is not None: write(_filter(_v, rawExpr=u'$checkbox($config)')) # from line 64, col 5.
                write(u'''
''')
            elif VFFSL(SL,"config.data.type",True) == "multicheckbox": # generated from line 65, col 4
                write(u'''\t\t\t\t''')
                _v = VFFSL(SL,"multicheckbox",False)(VFFSL(SL,"config",True)) # u'$multicheckbox($config)' on line 66, col 5
                if _v is not None: write(_filter(_v, rawExpr=u'$multicheckbox($config)')) # from line 66, col 5.
                write(u'''
''')
            elif VFFSL(SL,"config.data.type",True) == "number": # generated from line 67, col 4
                write(u'''\t\t\t\t''')
                _v = VFFSL(SL,"number",False)(VFFSL(SL,"config",True)) # u'$number($config)' on line 68, col 5
                if _v is not None: write(_filter(_v, rawExpr=u'$number($config)')) # from line 68, col 5.
                write(u'''
''')
        write(u'''\t</table>
</div>
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

    _mainCheetahMethod_for_config= 'respond'

## END CLASS DEFINITION

if not hasattr(config, '_initCheetahAttributes'):
    templateAPIClass = getattr(config, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(config)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=config()).run()


