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
__CHEETAH_genTime__ = 1364979192.921604
__CHEETAH_genTimestamp__ = 'Wed Apr  3 17:53:12 2013'
__CHEETAH_src__ = '/home/fermi/Work/Model/tmsingle/openpli3.0/build-tmsingle/tmp/work/mips32el-oe-linux/enigma2-plugin-extensions-openwebif-0.1+git1+279a2577c3bc6defebd4bf9e61a046dcf7f37c01-r0.72/git/plugin/controllers/views/ajax/edittimer.tmpl'
__CHEETAH_srcLastModified__ = 'Wed Apr  3 17:10:17 2013'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class edittimer(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(edittimer, self).__init__(*args, **KWs)
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
        
        write(u'''<form>
<div>
\t<div class="timerlist_row">
\t\t<span style="width: 100px; float: left;">Name:</span>
\t\t<span><input type="text" name="timername" id="timername" style="width: 450px;" class="text ui-widget-content ui-corner-all" /></span>
\t</div>
\t
\t<div class="timerlist_row">
\t\t<span style="width: 100px; float: left;">Description:</span>
\t\t<span><textarea name="description" id="description" style="width: 450px; height: 50px;" class="text ui-widget-content ui-corner-all" /></span>
\t</div>
\t
\t<div class="timerlist_row">
\t<span style="width: 100px; float: left;">Channel:</span>
\t\t<span>
\t\t<select id="bouquet_select" name="bouquet_select">
\t\t\t<option value="0">Nothing</option>
\t\t</select>
\t\t</span>
\t</div>
\t
\t<div class="timerlist_row">
\t\t<span style="width: 100px; float: left;">Start:</span>
\t\t<span>
\t\t<input type="text" name="timerbegin" id="timerbegin" value="" class="text ui-widget-content ui-corner-all" />
\t\t</span>
\t</div>

\t<div class="timerlist_row">
\t\t<span style="width: 100px; float: left;">End:</span>
\t\t<span>
\t\t<input type="text" name="timerend" id="timerend" value="" class="text ui-widget-content ui-corner-all" />
\t\t</span>
\t</div>
\t
\t<div class="timerlist_row">
\t\t<span style="width: 100px; float: left; block: inline;">Enabled:</span>
\t\t<span style="margin: 5px;">
\t\t\t<input type="checkbox" name="enabled" id="enabled" value="0" />
\t\t</span>
\t</div>
\t
\t<div class="timerlist_row">
\t\t<span style="width: 100px; float: left;">Just play:</span>
\t\t<span style="margin: 5px;">
\t\t\t<input type="checkbox" name="justplay" id="justplay" value="0" />
\t\t</span>
\t</div>
\t
\t<div class="timerlist_row">
\t\t<span style="width: 100px; float: left;">Repeated:</span>
\t\t<span id="repeatdays" style="margin: 5px;">
''')
        i = 0
        for day in ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']: # generated from line 54, col 3
            value = 2 ** VFFSL(SL,"i",True)
            write(u'''\t\t\t<input type="checkbox" name="repeated" id="day''')
            _v = VFFSL(SL,"i",True) # u'$i' on line 56, col 50
            if _v is not None: write(_filter(_v, rawExpr=u'$i')) # from line 56, col 50.
            write(u'''" value="''')
            _v = VFFSL(SL,"value",True) # u'$value' on line 56, col 61
            if _v is not None: write(_filter(_v, rawExpr=u'$value')) # from line 56, col 61.
            write(u'''" /><label for="day''')
            _v = VFFSL(SL,"i",True) # u'$i' on line 56, col 86
            if _v is not None: write(_filter(_v, rawExpr=u'$i')) # from line 56, col 86.
            write(u'''">''')
            _v = VFFSL(SL,"day",True) # u'$day' on line 56, col 90
            if _v is not None: write(_filter(_v, rawExpr=u'$day')) # from line 56, col 90.
            write(u'''</label>
''')
            i = VFFSL(SL,"i",True)+1
        write(u'''\t\t</span>
\t</div>
\t
\t<div class="timerlist_row">
\t\t<span style="width: 100px; float: left;">Location:</span>
\t\t<span>
\t\t<select id="dirname" name="dirname">
\t\t\t<option value="None">Default</option>
\t\t</select>
\t\t</span>
\t</div>
\t
\t<div class="timerlist_row">
\t\t<span style="width: 100px; float: left;">Tags:</span>
\t\t<span id="tagsnew" style="margin:5px">
\t\t</span>
\t</div>
\t
\t<div class="timerlist_row">
\t\t<span style="width: 100px; float: left;">After Event:</span>
\t\t<span>
\t\t<select id="afterevent" name="afterevent">
\t\t\t<option value="0">Nothing</option>
\t\t\t<option value="1">Standby</option>
\t\t\t<option value="2">Shutdown</option>
\t\t\t<option value="3" selected="">Auto</option>
\t\t</select>
\t\t</span>
\t</div>
\t<div id="errorbox" class="timerlist_row" style="color: red;">
\t\t<div class="ui-state-error ui-corner-all" style="padding: 0 .7em;"> 
\t\t\t<p><span class="ui-icon ui-icon-alert" style="float: left; margin-right: .3em;"></span> 
\t\t\t<span id="error"></span>
\t\t</div>
\t</div>
</div>
</form>

<script src="/js/jquery.timerpicker.js"></script>

<script type="text/javascript">


$(\'#timerbegin\').datetimepicker({
\tdateFormat: \'dd.mm.yy\',
\ttimeFormat: \'hh:mm\',
\tonClose: function(dateText, inst) {
\t\tif ($(\'#timerend\').val() != \'\' &&
\t\t\t$(this).datetimepicker(\'getDate\') > $(\'#timerend\').datetimepicker(\'getDate\')) {
\t\t\t\t$(\'#error\').text("Start time is after end time");
\t\t\t\t$(\'#errorbox\').show();
\t\t}
\t\telse
\t\t\t$(\'#errorbox\').hide();
\t}
});
$(\'#timerend\').datetimepicker({
\tdateFormat: \'dd.mm.yy\',
\ttimeFormat: \'hh:mm\',
\tonClose: function(dateText, inst) {
\t\tif ($(\'#timerbegin\').val() != \'\' &&\t
\t\t\t$(\'#timerbegin\').datetimepicker(\'getDate\') > $(this).datetimepicker(\'getDate\')) {
\t\t\t\t$(\'#error\').text("Start time is after end time");
\t\t\t\t$(\'#errorbox\').show();
\t\t}
\t\telse
\t\t\t$(\'#errorbox\').hide();
\t}
});

$(\'#repeatdays\').buttonset();

$(\'#editTimerForm\').dialog({
\tautoOpen: false,
\theight: 455,
\twidth: 600,
\tmodal: true,
\tbuttons: {
\t\t"Save": function() {
\t\t\tvar begindate = new Date($(\'#timerbegin\').datetimepicker(\'getDate\'));\t\t\t\t
\t\t\tvar enddate = new Date($(\'#timerend\').datetimepicker(\'getDate\'));

\t\t\tvar repeated = 0;
\t\t\t$(\'[name="repeated"]:checked\').each(function() {
\t\t\t\trepeated += parseInt($(this).val());
\t\t\t});
\t\t\tvar tags = "";
\t\t\t$(\'[name="tagsnew"]:checked\').each(function() {
\t\t\t\tif(tags!="")
\t\t\t\t\ttags+=" ";
\t\t\t\ttags += $(this).val();
\t\t\t\t
\t\t\t});
\t\t\tvar urldata = { sRef: $(\'#bouquet_select\').val(),
\t\t\t\tbegin: Math.round(begindate.getTime() / 1000),
\t\t\t\tend: Math.round(enddate.getTime() / 1000),
\t\t\t\tname: $(\'#timername\').val(),
\t\t\t\tdescription: $(\'#description\').val(),
\t\t\t\tdisabled: ($(\'#enabled\').is(\':checked\')?"0":"1"),
\t\t\t\tjustplay: ($(\'#justplay\').is(\':checked\')?"1":"0"),
\t\t\t\tafterevent: $(\'#afterevent\').val(),
\t\t\t\tdirname: $(\'#dirname\').val(),
\t\t\t\ttags: tags,
\t\t\t\trepeated: repeated };
\t\t\t
\t\t\tvar canclose = false;
\t\t\tif (current_serviceref == "") {
\t\t\t\t$.ajax({
\t\t\t\t\tasync: false,
\t\t\t\t\turl: "/api/timeradd?",
\t\t\t\t\tdata: urldata,
\t\t\t\t\tsuccess: function(data) {
\t\t\t\t\t\tresult = $.parseJSON(data);
\t\t\t\t\t\tif (result.result) {
\t\t\t\t\t\t\tcanclose = true;
\t\t\t\t\t\t}
\t\t\t\t\t\telse {
\t\t\t\t\t\t\t$("#error").text(result.message);
\t\t\t\t\t\t\t$("#errorbox").show();
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t});
\t\t\t}
\t\t\telse {
\t\t\t\turldata[\'channelOld\'] = current_serviceref;
\t\t\t\turldata[\'beginOld\'] = Math.round(current_begin);
\t\t\t\turldata[\'endOld\'] = Math.round(current_end);
\t\t\t\t$.ajax({
\t\t\t\t\tasync: false,
\t\t\t\t\turl: "/api/timerchange?",
\t\t\t\t\tdata: urldata,
\t\t\t\t\tsuccess: function(data) {
\t\t\t\t\t\tresult = $.parseJSON(data);
\t\t\t\t\t\tif (result.result) {
\t\t\t\t\t\t\tcanclose = true;
\t\t\t\t\t\t}
\t\t\t\t\t\telse {
\t\t\t\t\t\t\t$("#error").text(result.message);
\t\t\t\t\t\t\t$("#errorbox").show();
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t});
\t\t\t}
\t\t\t
\t\t\tif (canclose) {
\t\t\t\tif (reloadTimers) $("#content_container").load("/ajax/timers");
\t\t\t\t$(this).dialog("close");
\t\t\t}
\t\t},
\t\tCancel: function() {
\t\t\t$(this).dialog("close");
\t\t}
\t},
\tclose: function() {
\t\treturn;
\t}
});


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

    _mainCheetahMethod_for_edittimer= 'respond'

## END CLASS DEFINITION

if not hasattr(edittimer, '_initCheetahAttributes'):
    templateAPIClass = getattr(edittimer, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(edittimer)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=edittimer()).run()


