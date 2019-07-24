__author__ = 'samsjang@naver.com'

from os import path, listdir, remove
from urllib2 import urlopen, Request
from urlparse import urlparse, parse_qs
import sys


KSIZE = 1024
MSIZE = 1024*1024

MYTUBE_LOGO = None
AVOIDS = ['#', '<', '$', '+', '%', '>', '!', '`', '&', '*', '\'', '|', '{', '}',\
		'?', '"', '=', '/', ':', '\\', ' ', '@']


def convertURL(url):
	try:
		if url.split('/')[2] == 'youtu.be':
			videoid = url.split('/')[3]	
		else:
			videoid = parse_qs(urlparse(url).query)['v'][0]	
			
		url = 'http://www.youtube.com/get_video_info?video_id=' + videoid	
	except:		
		return None
		
	return url


def download(gui, url, folder):	
	gui.statusmsg.set('Start Download..')		
	
	url = convertURL(url)	
	
	if url is None:
		gui.statusmsg.set('Parsing URL Error.. Try another Video URL')
		return
	
	h = urlopen(url)
	data = h.read()	
	info = parse_qs(data)
	
	try:
		title = info['title'][0]
	except:
		title = 'MyTube'
		
	for c in AVOIDS:
		if c in title:
			title = title.replace(c, '')
	
	title = title.decode('utf-8')
	gui.vtitlemsg.set(title)
	
	try:
		if folder != '':		
			fname = folder + '/' + title + '.mp4'
		else:
			fname = title + '.mp4'
	except:
		self.statusmsg('Cannot parsing Video Title..Set Default Video Title')			
	
	try:
		stream_map = info['url_encoded_fmt_stream_map'][0]	
		video_info = stream_map.split(',')
	except:
		self.statusmsg('SORRY: Cannot extract video information.. Try another Video')
		return
	
	
	
	try:
		for video in video_info:
			item = parse_qs(video)
			#print item
			#print item['quality'][0]
			#print item['type'][0]
			#print item['url'][0]
			#print item['s'][0]
			
			url = item['url'][0]
			#req = Request(url)
			#req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.9 Safari/533.2')
			#h = urlopen(req)
			h = urlopen(url)
			size = int(h.headers['Content-Length'])			
			
			gui.progress['value'] = 0
			gui.progress['maximum'] = size
			#print size
			#print fname
			
			try:
				dfile = open(fname.encode(sys.getfilesystemencoding()), 'wb+')
			except:
				dfile = open('download.mp4', 'wb+')
				
			downloaded = 0
			buf = h.read(KSIZE)
			
			while gui.flag and buf:
				dfile.write(buf)		
				downloaded += KSIZE
				gui.progress['value'] = downloaded
				gui.statusmsg.set('Downloading.. [%d]/[%d]MB' %((downloaded/MSIZE), (size/MSIZE)))
				buf = h.read(KSIZE)
			
			h.close()
			dfile.close()		
			gui.progress['value'] = 0
			
			if gui.flag:
				gui.statusmsg.set('Download Complete!!')
			else:
				gui.statusmsg.set('Downloading Canceled by User!')
				remove(fname)
		
			break
	except Exception,e :
		gui.statusmsg.set('Errors During Download: %s' %e)
		return