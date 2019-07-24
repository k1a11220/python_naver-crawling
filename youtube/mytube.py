__author__ = 'samsjang@naver.com'

from tkinter import *
import ttk
import tkFileDialog as fd
from PIL import ImageTk, Image
from threading import Event, Thread
from downloader import download

VER = 'v0.2'


# GUI for MyTube
class MyTube():
	def __init__(self):
		self.flag = True # flag for terminate thread	
		global MYTUBE_LOGO
		self.saveto = ''		
		
		self.root = Tk()
		self.root.title('Youtube Video Downloader-MyTube %s' %VER)
		self.root.resizable(width=FALSE, height=FALSE)
		
		self.statusmsg = StringVar()		
		self.statusmsg.set('Waiting..')
		self.vtitlemsg = StringVar()
		self.vtitlemsg.set('Youtube Video Title')
		
		# Main Frame & Panels
		content = ttk.Frame(self.root, padding=(6, 6, 6, 6))				
		content.grid(column=0, row=0, sticky=(N, W, E, S))
		
		logo_panel = ttk.Frame(content, padding=(3,3,3,3))
		url_panel = ttk.Frame(content, relief='groove', padding=(6,6,6,6))
		status_panel = ttk.Frame(content, relief='groove', padding=(6,6,10,10))
		progress_panel = ttk.Frame(content, relief='groove', padding=(6,6,6,6))
		
		logo_panel.grid(column=0, row=0, sticky=(N, W, E, S))
		url_panel.grid(column=0, row=1, sticky=(N, W, E, S))
		status_panel.grid(column=0, row=2, sticky=(N, W, E, S))
		progress_panel.grid(column=0, row=3, sticky=(N, W, E, S))		
		
		
		# Create Logo
		try:
			MYTUBE_LOGO = ImageTk.PhotoImage(Image.open('resources/mytube.jpg'))
		except:
			pass
			
		logolabel = ttk.Label(logo_panel, image=MYTUBE_LOGO)		
		logolabel.grid(column=0, row=0, sticky=(N, W, E, S))
		
		
		# Create Label		
		url_label = ttk.Label(url_panel, text='Video URL:', anchor=W)
		saveto_label = ttk.Label(url_panel, text='Save to:', anchor=W)
		vtitle_label = ttk.Label(status_panel, text='Video Title:', anchor=W)
		status_label = ttk.Label(status_panel, text='Status:', anchor=W)
		progress_label = ttk.Label(progress_panel, text='Progress:', anchor=W)
		
		# Create Entry Widget for input video URL		
		self.urlentry = ttk.Entry(url_panel, width=70)
		self.savetoentry = ttk.Entry(url_panel, width=45)		
		
		# Create Progressbar
		self.progress = ttk.Progressbar(progress_panel, orient=HORIZONTAL, length=330, mode='determinate')		
		
		# Create vTitle & Status Message
		self.vtitle = ttk.Label(status_panel, textvariable=self.vtitlemsg, anchor=W)
		self.status = ttk.Label(status_panel, textvariable=self.statusmsg, anchor=W)
				
		# Create Buttons		
		folder_button = ttk.Button(url_panel, text="Folder", command=self.folder)		
		start_button = ttk.Button(progress_panel, text="Start", command=self.start)	
		cancel_button = ttk.Button(progress_panel, text="Cancel", command=self.cancel)		
		
		# Locate widges for URL Panel
		url_label.grid(column=0, row=0, sticky=W)
		self.urlentry.grid(column=1, row=0, columnspan=2, pady=10, sticky=W)
		saveto_label.grid(column=0, row=1, sticky=W)
		self.savetoentry.grid(column=1, row=1, sticky=W)
		folder_button.grid(column=2, row=1, stick=W)
		
		# Locate widgets for Status Panel
		vtitle_label.grid(column=0, row=0, padx=5, pady=10, sticky=W)
		self.vtitle.grid(column=1, row=0, sticky=W)
		status_label.grid(column=0, row=1, padx=5, sticky=W)
		self.status.grid(column=1, row=1, sticky=W)		
		
		# Locate Widges for Progressbar
		progress_label.grid(column=0, row=0, sticky=W)
		self.progress.grid(column=1, row=0, sticky=W)
		start_button.grid(column=2, row=0, padx=45, sticky=W)
		#cancel_button.grid(column=3, row=0, sticky=E)		
		
		#self.root.columnconfigure(0, weight=1)
		#self.root.rowconfigure(0, weight=1)
		#content.columnconfigure(0, weight=1)
		#content.columnconfigure(1, weight=1)	
		#content.rowconfigure(0, weight=1)
		#content.rowconfigure(1, weight=1)	

			
	# Function for Folder Button
	def folder(self, *args):
		self.saveto = fd.askdirectory()		
		
		if self.saveto == '':			
			return
		
		self.savetoentry.delete(0, END)
		self.savetoentry.insert(0, self.saveto)	
		
	
	# Start Thread for downloading function
	def start(self, *args):
		url = self.urlentry.get()
		
		if url == '':
			self.statusmsg.set('Enter Youtube URL for downloading Video!!')
			return
		
		thread = Thread(target=download, args=[self, url, self.saveto])			
		thread.setDaemon(False)
		thread.start()		
	
		
	# Function for Cancel Button
	def cancel(self, *args):
		self.flag = False	
	
		
	def run(self):
		self.root.mainloop()	


if __name__ == '__main__':
	obj = MyTube()
	obj.run()