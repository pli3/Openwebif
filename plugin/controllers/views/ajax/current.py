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
__CHEETAH_genTime__ = 1364979193.719331
__CHEETAH_genTimestamp__ = 'Wed Apr  3 17:53:13 2013'
__CHEETAH_src__ = '/home/fermi/Work/Model/tmsingle/openpli3.0/build-tmsingle/tmp/work/mips32el-oe-linux/enigma2-plugin-extensions-openwebif-0.1+git1+279a2577c3bc6defebd4bf9e61a046dcf7f37c01-r0.72/git/plugin/controllers/views/ajax/current.tmpl'
__CHEETAH_srcLastModified__ = 'Wed Apr  3 17:10:17 2013'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class current(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(current, self).__init__(*args, **KWs)
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
        
        write(u'''<!-- OSD -->
<div style="width:680px;height:137px;background-image:url(/images/osd/osd_back.png);">
  <div style="float:left;width:120px;height:137px;">
    <div style="float:left;display:block;width:120px;height:37px;">
      <div style="position:relative;top:10px;left:18px;color:#FFF;font-size:13px;font-weight:bold;">''')
        _v = VFFSL(SL,"info.date",True) # u'$info.date' on line 5, col 101
        if _v is not None: write(_filter(_v, rawExpr=u'$info.date')) # from line 5, col 101.
        write(u'''</div>
    </div>
    <div style="float:left;display:block;width:120px;height:60px;">
      <div style="position:relative;top:0px;left:15px;"><img border=\'0\' width="100px" height="60px" src=\'''')
        _v = VFFSL(SL,"getVar",False)("info.picon", "/images/default_picon.png") # u'$getVar("info.picon", "/images/default_picon.png")' on line 8, col 106
        if _v is not None: write(_filter(_v, rawExpr=u'$getVar("info.picon", "/images/default_picon.png")')) # from line 8, col 106.
        write(u'''\' onclick="open_epg_pop(\'''')
        _v = VFFSL(SL,"info.ref",True) # u'$info.ref' on line 8, col 181
        if _v is not None: write(_filter(_v, rawExpr=u'$info.ref')) # from line 8, col 181.
        write(u'''\');" href="#" title="Show EPG for ''')
        _v = VFFSL(SL,"info.name",True) # u'$info.name' on line 8, col 224
        if _v is not None: write(_filter(_v, rawExpr=u'$info.name')) # from line 8, col 224.
        write(u'''" border="0" alt=\'\' /></div>
    </div>
    <div style="float:left;display:block;width:120px;height:40px;">
      <div style="position:relative;top:8px;left:0px;color:#FFF;text-align:center;font-size:13px;font-weight:bold;">''')
        _v = VFFSL(SL,"info.provider",True) # u'$info.provider' on line 11, col 117
        if _v is not None: write(_filter(_v, rawExpr=u'$info.provider')) # from line 11, col 117.
        write(u'''</div>
    </div>
  </div>
  <div style="float:left;width:560px;height:137px;">
    <div style="float:left;width:560px;height:25px;">
      <div style="float:left;position:relative;top:5px;left:0px;width:480px;color:#FFF;text-align:center;font-size:18px;"><a style="color:#FFF" target="_blank" title="Stream ''')
        _v = VFFSL(SL,"getVar",False)('now.title', '') # u"$getVar('now.title', '')" on line 16, col 175
        if _v is not None: write(_filter(_v, rawExpr=u"$getVar('now.title', '')")) # from line 16, col 175.
        write(u''' from ''')
        _v = VFFSL(SL,"info.name",True) # u'$info.name' on line 16, col 205
        if _v is not None: write(_filter(_v, rawExpr=u'$info.name')) # from line 16, col 205.
        write(u'''" href=\'/web/stream.m3u?ref=''')
        _v = VFFSL(SL,"info.ref",True) # u'$info.ref' on line 16, col 243
        if _v is not None: write(_filter(_v, rawExpr=u'$info.ref')) # from line 16, col 243.
        write(u'''&name=''')
        _v = VFFSL(SL,"info.name",True) # u'$info.name' on line 16, col 258
        if _v is not None: write(_filter(_v, rawExpr=u'$info.name')) # from line 16, col 258.
        write(u"""'>""")
        _v = VFFSL(SL,"info.name",True) # u'$info.name' on line 16, col 270
        if _v is not None: write(_filter(_v, rawExpr=u'$info.name')) # from line 16, col 270.
        write(u'''</a></div>
    </div>
    <div style="float:left;width:560px;height:24px;">
      <div style="float:left;width:70px;height:24px;">
        <div style="position:relative;top:10px;left:15px;color:#FFF;font-size:14px;">''')
        _v = VFFSL(SL,"getVar",False)("now.begin", " ") # u'$getVar("now.begin", " ")' on line 20, col 86
        if _v is not None: write(_filter(_v, rawExpr=u'$getVar("now.begin", " ")')) # from line 20, col 86.
        write(u'''</div>
      </div>
      <div style="float:left;width:360px;height:24px;">
        <div style="position:relative;top:10px;left:0px;color:#FFF;font-size:14px;">''')
        _v = VFFSL(SL,"getVar",False)("now.title", " ") # u'$getVar("now.title", " ")' on line 23, col 85
        if _v is not None: write(_filter(_v, rawExpr=u'$getVar("now.title", " ")')) # from line 23, col 85.
        write(u'''</div>
      </div>
      <div style="float:left;width:130px;height:24px;">
        <div style="position:relative;top:10px;left:0px;color:#FFF;font-size:14px;">+''')
        _v = VFFSL(SL,"getVar",False)("now.tleft", " ") # u'$getVar("now.tleft", " ")' on line 26, col 86
        if _v is not None: write(_filter(_v, rawExpr=u'$getVar("now.tleft", " ")')) # from line 26, col 86.
        write(u''' min</div>
      </div>
    </div>
    <div style="float:left;width:560px;height:16px;">
      <div style="float:left;position:relative;top:2px;left:15px;width:400px;height:14px;background-image:url(/images/osd/chan_bar_back.png);">
        <div style="float:left;width:400px;height:14px;"><img border=\'0\' height=\'14px\' width=\'''')
        _v = VFFSL(SL,"getVar",False)("now.progress", "0") # u'${getVar("now.progress", "0")}' on line 31, col 95
        if _v is not None: write(_filter(_v, rawExpr=u'${getVar("now.progress", "0")}')) # from line 31, col 95.
        write(u'''px\' src=\'/images/osd/chan_bar.png\' alt=\'\' /></div>
      </div>
    </div>
    <div style="float:left;width:560px;height:14px;">
      <div style="float:left;width:70px;height:14px;">
        <div style="position:relative;top:0px;left:15px;height:14px;color:#FFF;font-size:14px;">''')
        _v = VFFSL(SL,"getVar",False)("next.begin", " ") # u'$getVar("next.begin", " ")' on line 36, col 97
        if _v is not None: write(_filter(_v, rawExpr=u'$getVar("next.begin", " ")')) # from line 36, col 97.
        write(u'''</div>
      </div>
      <div style="float:left;width:360px;height:14px;">
        <div style="position:relative;top:0px;left:0px;height:14px;color:#FFF;font-size:14px;">''')
        _v = VFFSL(SL,"getVar",False)("next.title", " ") # u'$getVar("next.title", " ")' on line 39, col 96
        if _v is not None: write(_filter(_v, rawExpr=u'$getVar("next.title", " ")')) # from line 39, col 96.
        write(u'''</div>
      </div>
      <div style="float:left;width:130px;height:14px;">
        <div style="position:relative;top:0px;left:0px;height:14px;color:#FFF;font-size:14px;">&nbsp; ''')
        _v = VFFSL(SL,"getVar",False)("next.duration", " ") # u'$getVar("next.duration", " ")' on line 42, col 103
        if _v is not None: write(_filter(_v, rawExpr=u'$getVar("next.duration", " ")')) # from line 42, col 103.
        write(u''' min</div>
      </div>
    </div>
    <div style="float:left;width:560px;height:20px;">
      <div style="float:left;width:100px;height:20px;">
        <div style="position:relative;top:6px;left:15px;height:14px;color:#FFF;font-size:14px;">''')
        _v = VFFSL(SL,"getVar",False)("info.tunertype", " ") # u'$getVar("info.tunertype", " ")' on line 47, col 97
        if _v is not None: write(_filter(_v, rawExpr=u'$getVar("info.tunertype", " ")')) # from line 47, col 97.
        write(u'''</div>
      </div>
      <div style="float:left;width:80px;height:20px;">
        <div style="float:left;position:relative;top:6px;left:0px;height:14px;color:#FFF;font-size:14px;">Snr: ''')
        _v = VFFSL(SL,"getVar",False)("info.snr", "0") # u'$getVar("info.snr", "0")' on line 50, col 112
        if _v is not None: write(_filter(_v, rawExpr=u'$getVar("info.snr", "0")')) # from line 50, col 112.
        write(u''' % </div>
      </div>
      <div style="float:left;width:100px;height:20px;">
        <div style="float:left;position:relative;top:8px;left:0px;width:100px;height:14px;background-image:url(/images/osd/snr_bar_back.png);">
          <div style="float:left;width:100px;height:14px;"><img border=\'0\' height=\'14px\' width=\'''')
        _v = VFFSL(SL,"getVar",False)("info.snr", "0") # u'${getVar("info.snr", "0")}' on line 54, col 97
        if _v is not None: write(_filter(_v, rawExpr=u'${getVar("info.snr", "0")}')) # from line 54, col 97.
        write(u'''px\' src=\'/images/osd/chan_bar.png\' alt=\'\' /></div>
        </div>
      </div>
      <div style="float:left;width:100px;height:20px;">
        <div style="float:left;position:relative;top:6px;left:7px;height:14px;color:#FFF;font-size:14px;"> Ber: ''')
        _v = VFFSL(SL,"getVar",False)("info.ber", "N/A") # u'$getVar("info.ber", "N/A")' on line 58, col 113
        if _v is not None: write(_filter(_v, rawExpr=u'$getVar("info.ber", "N/A")')) # from line 58, col 113.
        write(u''' </div>
      </div>
      <div style="float:left;width:125px;height:20px;">
        <div style="position:relative;top:6px;left:0px;height:14px;color:#FFF;font-size:14px;">''')
        _v = VFFSL(SL,"info.width",True) # u'$info.width' on line 61, col 96
        if _v is not None: write(_filter(_v, rawExpr=u'$info.width')) # from line 61, col 96.
        write(u''' x ''')
        _v = VFFSL(SL,"info.height",True) # u'$info.height' on line 61, col 110
        if _v is not None: write(_filter(_v, rawExpr=u'$info.height')) # from line 61, col 110.
        write(u'''</div>
      </div>
    </div>
    <div style="float:left;width:560px;height:60px;">
      <div style="float:left;width:110px;height:26px;">
        <div style="float:left;position:relative;top:6px;left:15px;height:26px;color:#FFF;font-size:14px;">
''')
        if VFFSL(SL,"info.tunernumber",True) == 0: # generated from line 67, col 1
            write(u"""          <img border='0' src='/images/osd/icon_a.png' alt='' />
          <img border='0' src='/images/osd/icon_b_off.png' alt='' />
          <img border='0' src='/images/osd/icon_c_off.png' alt='' />
          <img border='0' src='/images/osd/icon_d_off.png' alt='' />
""")
        elif VFFSL(SL,"info.tunernumber",True) == 1: # generated from line 72, col 1
            write(u"""          <img border='0' src='/images/osd/icon_a_off.png' alt='' />
          <img border='0' src='/images/osd/icon_b.png' alt='' />
          <img border='0' src='/images/osd/icon_c_off.png' alt='' />
          <img border='0' src='/images/osd/icon_d_off.png' alt='' />
""")
        elif VFFSL(SL,"info.tunernumber",True) == 2: # generated from line 77, col 1
            write(u"""          <img border='0' src='/images/osd/icon_a_off.png' alt='' />
          <img border='0' src='/images/osd/icon_b_off.png' alt='' />
          <img border='0' src='/images/osd/icon_c.png' alt='' />
          <img border='0' src='/images/osd/icon_d_off.png' alt='' />
""")
        elif VFFSL(SL,"info.tunernumber",True) == 3: # generated from line 82, col 1
            write(u"""          <img border='0' src='/images/osd/icon_a_off.png' alt='' />
          <img border='0' src='/images/osd/icon_b_off.png' alt='' />
          <img border='0' src='/images/osd/icon_c_off.png' alt='' />
          <img border='0' src='/images/osd/icon_d.png' alt='' />
""")
        write(u'''        </div>
      </div>
      <div style="float:left;width:400px;height:32px;">
        <div style="float:left;position:relative;top:6px;left:10px;height:26px;color:#FFF;font-size:14px;">
''')
        if VFFSL(SL,"info.crypt",True) == 1: # generated from line 92, col 1
            write(u"""          <img border='0' src='/images/osd/icon_crypt.png' alt='' />
""")
        else: # generated from line 94, col 1
            write(u"""          <img border='0' src='/images/osd/icon_crypt_off.png' alt='' />
""")
        if VFFSL(SL,"info.dolby",True) == True: # generated from line 97, col 1
            write(u"""          <img border='0' src='/images/osd/icon_dolby.png' alt='' />
""")
        else: # generated from line 99, col 1
            write(u"""          <img border='0' src='/images/osd/icon_dolby_off.png' alt='' />
""")
        if VFFSL(SL,"info.wide",True) == True: # generated from line 102, col 1
            write(u"""          <img border='0' src='/images/osd/icon_format.png' alt='' />
""")
        else: # generated from line 104, col 1
            write(u"""          <img border='0' src='/images/osd/icon_format_off.png' alt='' />
""")
        if VFFSL(SL,"info.width",True) > 1900: # generated from line 107, col 1
            write(u"""          <img border='0' src='/images/osd/icon_hd.png' alt='' />
""")
        else: # generated from line 109, col 1
            write(u"""          <img border='0' src='/images/osd/icon_sd.png' alt='' />
""")
        if VFFSL(SL,"info.txtpid",True) != "N/A": # generated from line 112, col 1
            write(u"""          <img border='0' src='/images/osd/icon_txt.png' alt='' />
""")
        else: # generated from line 114, col 1
            write(u"""          <img border='0' src='/images/osd/icon_txt_off.png' alt='' />
""")
        if VFFSL(SL,"info.subs",True) == True: # generated from line 117, col 1
            write(u"""          <img border='0' src='/images/osd/icon_sub.png' alt='' />
""")
        else: # generated from line 119, col 1
            write(u"""          <img border='0' src='/images/osd/icon_sub_off.png' alt='' />
""")
        if VFFSL(SL,"info.rec_state",True) == True: # generated from line 122, col 1
            write(u"""          <img border='0' src='/images/osd/icon_rec.png' alt='' />
""")
        else: # generated from line 124, col 1
            write(u"""          <img border='0' src='/images/osd/icon_rec_off.png' alt='' />
""")
        write(u'''        </div>
      </div>
    </div>
  </div>
</div>

<!-- /END OSD -->
 

<br />
<table style="background: #1C478E;font-size:12px;" width="100%" border="0" cellspacing="1" cellpadding="5">
\t
\t\t\t<tr>
\t\t\t\t<th colspan="3" class="infoHeader">Service</th>
\t\t\t</tr>
\t\t\t<tr style="background-color:  #f0f7fc;">
\t\t\t\t<td>Name: ''')
        _v = VFFSL(SL,"info.name",True) # u'$info.name' on line 143, col 15
        if _v is not None: write(_filter(_v, rawExpr=u'$info.name')) # from line 143, col 15.
        write(u'''</td>
\t\t\t\t<td>Provider: ''')
        _v = VFFSL(SL,"info.provider",True) # u'$info.provider' on line 144, col 19
        if _v is not None: write(_filter(_v, rawExpr=u'$info.provider')) # from line 144, col 19.
        write(u'''</td>
\t\t\t\t<td>Namespace: ''')
        _v = VFFSL(SL,"info.namespace",True) # u'$info.namespace' on line 145, col 20
        if _v is not None: write(_filter(_v, rawExpr=u'$info.namespace')) # from line 145, col 20.
        write(u'''</td>
\t\t\t</tr>
\t\t\t<tr style="background-color:  #f0f7fc;">
\t\t\t\t<td>Video Width: ''')
        _v = VFFSL(SL,"info.width",True) # u'$info.width' on line 148, col 22
        if _v is not None: write(_filter(_v, rawExpr=u'$info.width')) # from line 148, col 22.
        write(u'''</td>
\t\t\t\t<td>Video Height: ''')
        _v = VFFSL(SL,"info.height",True) # u'$info.height' on line 149, col 23
        if _v is not None: write(_filter(_v, rawExpr=u'$info.height')) # from line 149, col 23.
        write(u'''</td>
\t\t\t\t<td>Video Wide: ''')
        _v = VFFSL(SL,"info.wide",True) # u'$info.wide' on line 150, col 21
        if _v is not None: write(_filter(_v, rawExpr=u'$info.wide')) # from line 150, col 21.
        write(u'''</td>
\t\t\t</tr>
\t\t\t<tr style="background-color:  #f0f7fc;">
\t\t\t\t<td>Encrypted: ''')
        _v = VFFSL(SL,"info.crypt",True) # u'$info.crypt' on line 153, col 20
        if _v is not None: write(_filter(_v, rawExpr=u'$info.crypt')) # from line 153, col 20.
        write(u'''</td>
\t\t\t\t<td>Dolby: ''')
        _v = VFFSL(SL,"info.dolby",True) # u'$info.dolby' on line 154, col 16
        if _v is not None: write(_filter(_v, rawExpr=u'$info.dolby')) # from line 154, col 16.
        write(u'''</td>
\t\t\t\t<td>Subservices: ''')
        _v = VFFSL(SL,"info.subs",True) # u'$info.subs' on line 155, col 22
        if _v is not None: write(_filter(_v, rawExpr=u'$info.subs')) # from line 155, col 22.
        write(u'''</td>
\t\t\t</tr>\t\t\t
\t\t\t<tr style="background-color:  #f0f7fc;">
\t\t\t\t<td>Teletext: ''')
        _v = VFFSL(SL,"info.txtpid",True) # u'$info.txtpid' on line 158, col 19
        if _v is not None: write(_filter(_v, rawExpr=u'$info.txtpid')) # from line 158, col 19.
        write(u'''</td>
\t\t\t\t<td>Recording Status: ''')
        _v = VFFSL(SL,"info.rec_state",True) # u'$info.rec_state' on line 159, col 27
        if _v is not None: write(_filter(_v, rawExpr=u'$info.rec_state')) # from line 159, col 27.
        write(u'''</td>
\t\t\t\t<td>Pmtpid: ''')
        _v = VFFSL(SL,"info.pmtpid",True) # u'$info.pmtpid' on line 160, col 17
        if _v is not None: write(_filter(_v, rawExpr=u'$info.pmtpid')) # from line 160, col 17.
        write(u'''</td>
\t\t\t</tr>
\t\t\t<tr style="background-color:  #f0f7fc;">
\t\t\t\t<td>Apid: ''')
        _v = VFFSL(SL,"info.apid",True) # u'$info.apid' on line 163, col 15
        if _v is not None: write(_filter(_v, rawExpr=u'$info.apid')) # from line 163, col 15.
        write(u'''</td>
\t\t\t\t<td>Vpid: ''')
        _v = VFFSL(SL,"info.vpid",True) # u'$info.vpid' on line 164, col 15
        if _v is not None: write(_filter(_v, rawExpr=u'$info.vpid')) # from line 164, col 15.
        write(u'''</td>
\t\t\t\t<td>Pcrpid: ''')
        _v = VFFSL(SL,"info.pcrpid",True) # u'$info.pcrpid' on line 165, col 17
        if _v is not None: write(_filter(_v, rawExpr=u'$info.pcrpid')) # from line 165, col 17.
        write(u'''</td>
\t\t\t</tr>
\t\t\t<tr style="background-color:  #f0f7fc;">
\t\t\t\t<td>Tsid: ''')
        _v = VFFSL(SL,"info.tsid",True) # u'$info.tsid' on line 168, col 15
        if _v is not None: write(_filter(_v, rawExpr=u'$info.tsid')) # from line 168, col 15.
        write(u'''</td>
\t\t\t\t<td>Onid: ''')
        _v = VFFSL(SL,"info.onid",True) # u'$info.onid' on line 169, col 15
        if _v is not None: write(_filter(_v, rawExpr=u'$info.onid')) # from line 169, col 15.
        write(u'''</td>
\t\t\t\t<td>Sid: ''')
        _v = VFFSL(SL,"info.sid",True) # u'$info.sid' on line 170, col 14
        if _v is not None: write(_filter(_v, rawExpr=u'$info.sid')) # from line 170, col 14.
        write(u'''</td>
\t\t\t</tr>
\t\t\t\t
\t\t\t<tr>
\t\t\t\t<th colspan="3" class="infoHeader">Tuner Signal</th>
\t\t\t</tr>
\t\t\t<tr style="background-color:  #f0f7fc;">
\t\t\t\t<td>Tuner Type: ''')
        _v = VFFSL(SL,"getVar",False)("info.tunertype", "N/A") # u'$getVar("info.tunertype", "N/A")' on line 177, col 21
        if _v is not None: write(_filter(_v, rawExpr=u'$getVar("info.tunertype", "N/A")')) # from line 177, col 21.
        write(u'''</td>
\t\t\t\t<td>Tuner Number(0-3):  ''')
        _v = VFFSL(SL,"getVar",False)("info.tunernumber", "N/A") # u'$getVar("info.tunernumber", "N/A")' on line 178, col 29
        if _v is not None: write(_filter(_v, rawExpr=u'$getVar("info.tunernumber", "N/A")')) # from line 178, col 29.
        write(u'''</td>
\t\t\t\t<td>Tuner Signal Quality SNR:  ''')
        _v = VFFSL(SL,"getVar",False)("info.snr", "N/A") # u'$getVar("info.snr", "N/A")' on line 179, col 36
        if _v is not None: write(_filter(_v, rawExpr=u'$getVar("info.snr", "N/A")')) # from line 179, col 36.
        write(u'''</td>
\t\t\t</tr>
\t\t\t<tr style="background-color:  #f0f7fc;">
\t\t\t\t<td>Tuner Signal Quality SNR_DB:  ''')
        _v = VFFSL(SL,"getVar",False)("info.snr_db", "N/A") # u'$getVar("info.snr_db", "N/A")' on line 182, col 39
        if _v is not None: write(_filter(_v, rawExpr=u'$getVar("info.snr_db", "N/A")')) # from line 182, col 39.
        write(u'''</td>
\t\t\t\t<td>Tuner Signal Power AGC:  ''')
        _v = VFFSL(SL,"getVar",False)("info.agc", "N/A") # u'$getVar("info.agc", "N/A")' on line 183, col 34
        if _v is not None: write(_filter(_v, rawExpr=u'$getVar("info.agc", "N/A")')) # from line 183, col 34.
        write(u'''</td>
\t\t\t\t<td>Tuner Bit Error Rate BER:  ''')
        _v = VFFSL(SL,"getVar",False)("info.ber", "N/A") # u'$getVar("info.ber", "N/A")' on line 184, col 36
        if _v is not None: write(_filter(_v, rawExpr=u'$getVar("info.ber", "N/A")')) # from line 184, col 36.
        write(u'''</td>
\t\t\t</tr>
\t\t\t<tr>
\t\t\t\t<th colspan="3" class="infoHeader">Current Event</th>
\t\t\t</tr>
\t\t\t<tr style="background-color:  #f0f7fc;">
\t\t\t\t<td colspan="3">Title: ''')
        _v = VFFSL(SL,"getVar",False)("now.title", " ") # u'$getVar("now.title", " ")' on line 190, col 28
        if _v is not None: write(_filter(_v, rawExpr=u'$getVar("now.title", " ")')) # from line 190, col 28.
        write(u'''</td>
\t\t\t</tr>
\t\t\t<tr style="background-color:  #f0f7fc;">
\t\t\t\t<td>Begin: ''')
        _v = VFFSL(SL,"getVar",False)("now.begin", " ") # u'$getVar("now.begin", " ")' on line 193, col 16
        if _v is not None: write(_filter(_v, rawExpr=u'$getVar("now.begin", " ")')) # from line 193, col 16.
        write(u'''</td>
\t\t\t\t<td>End: ''')
        _v = VFFSL(SL,"getVar",False)("now.end", " ") # u'$getVar("now.end", " ")' on line 194, col 14
        if _v is not None: write(_filter(_v, rawExpr=u'$getVar("now.end", " ")')) # from line 194, col 14.
        write(u'''</td>
\t\t\t\t<td>Duration: ''')
        _v = VFFSL(SL,"getVar",False)("now.duration", " ") # u'$getVar("now.duration", " ")' on line 195, col 19
        if _v is not None: write(_filter(_v, rawExpr=u'$getVar("now.duration", " ")')) # from line 195, col 19.
        write(u'''</td>
\t\t\t</tr>
\t\t\t<tr style="background-color:  #f0f7fc;">
\t\t\t\t<td colspan="3">Description:  ''')
        _v = VFFSL(SL,"getVar",False)("now.shortdesc", " ") # u'$getVar("now.shortdesc", " ")' on line 198, col 35
        if _v is not None: write(_filter(_v, rawExpr=u'$getVar("now.shortdesc", " ")')) # from line 198, col 35.
        write(u'''</td>
\t\t\t</tr>
\t\t\t
</table>
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

    _mainCheetahMethod_for_current= 'respond'

## END CLASS DEFINITION

if not hasattr(current, '_initCheetahAttributes'):
    templateAPIClass = getattr(current, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(current)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=current()).run()

