##############################################################################
#                        2011 E2OpenPlugins                                  #
#                                                                            #
#  This file is open source software; you can redistribute it and/or modify  #
#     it under the terms of the GNU General Public License version 2 as      #
#               published by the Free Software Foundation.                   #
#                                                                            #
##############################################################################

from enigma import eServiceReference, iServiceInformation, eServiceCenter
from Components.Sources.Source import Source
from ServiceReference import ServiceReference
from Tools.FuzzyDate import FuzzyTime
from os import stat as os_stat, walk
from os.path import islink
from Components.config import config
from Components.MovieList import MovieList
from Tools.Directories import fileExists
from time import strftime, localtime

def getMovieList(directory=None, tag=None):
	movieliste = []
	
	if directory == None:
		directory = config.usage.default_path.value
	
	if directory[-1] != "/":
		directory += "/"
		
	root = eServiceReference("2:0:1:0:0:0:0:0:0:0:" + directory)

	bookmarklist=[x for x in walk(directory).next()[1] if (x[0] != '.' and not islink(directory+'/'+x))]
	bookmarklist.sort()
	
	tagfilter = []
	
	movielist = MovieList(None)
	movielist.load(root, None)
	
	if tag != None:
		movielist.reload(root=root, filter_tags=[tag])
	loadLength = True

	for (serviceref, info, begin, unknown) in movielist.list:
		if serviceref.flags & eServiceReference.mustDescent:
				continue

		rtime = info.getInfo(serviceref, iServiceInformation.sTimeCreate)

		if rtime > 0:
			t = FuzzyTime(rtime)
			begin_string = t[0] + ", " + t[1]
		else:
			begin_string = "undefined"

		try:
			Len = info.getLength(serviceref)
		except:
			Len = None

		if Len > 0:
			Len = "%d:%02d" % (Len / 60, Len % 60)
		else:
			Len = "?:??"
		
		sourceERef = info.getInfoString(serviceref, iServiceInformation.sServiceref)
		sourceRef = ServiceReference(sourceERef)

		event = info.getEvent(serviceref)
		ext = event and event.getExtendedDescription() or ""

		filename = '/'.join(serviceref.toString().split("/")[1:])
		servicename = ServiceReference(serviceref).getServiceName().replace('\xc2\x86', '').replace('\xc2\x87', '')
		movie = {}
		filename = '/'+filename
		movie['filename'] = filename
		movie['filename_stripped'] = filename.split("/")[-1]
		movie['eventname'] = servicename
		movie['description'] = info.getInfoString(serviceref, iServiceInformation.sDescription)
		movie['begintime'] = begin_string
		movie['serviceref'] = serviceref.toString()
		movie['length'] = Len
		movie['tags'] = info.getInfoString(serviceref, iServiceInformation.sTags)
		filename = filename.replace("'","\'").replace("%","\%")
		try:
			movie['filesize'] = os_stat(filename).st_size
		except:
			movie['filesize'] = 0
		movie['fullname'] = serviceref.toString()
		movie['descriptionExtended'] = ext
		movie['servicename'] = sourceRef.getServiceName().replace('\xc2\x86', '').replace('\xc2\x87', '')
		movie['recordingtime'] = rtime
		
		movieliste.append(movie)
		
	
	return { "movies": movieliste, "bookmarks": bookmarklist, "directory": directory }

def removeMovie(session, sRef):
	service = ServiceReference(sRef)
	result = False

	if service is not None:
		serviceHandler = eServiceCenter.getInstance()
		offline = serviceHandler.offlineOperations(service.ref)
		info = serviceHandler.info(service.ref)
		name = info and info.getName(service.ref) or "this recording"

	if offline is not None:
		if not offline.deleteFromDisk(0):
			result = True

	if result == False:
		return {
			"result": False,
			"message": "Could not delete Movie '%s'" % name
			}
	else:
		return {
			"result": True,
			"message": "The movie '%s' has been deleted successfully" % name
			}

def getMovieTags():
	tags = []
	if fileExists("/etc/enigma2/movietags"):
		for tag in open("/etc/enigma2/movietags").read().split("\n"):
			if len(tag.strip()) > 0:
				tags.append(tag.strip())
		
	return {
		"result": True,
		"tags": tags
	}