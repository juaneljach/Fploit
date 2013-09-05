import ftplib
import os
import socket
import sys
import wcolors

options = ["0.0.0.0",21]

def show_options(list):
	print "\nNAME\t\tSETTING\t\tDESCRIPTION"
	print "-----------\t-----------\t--------------"
	print "%s \t\t%s \t%s" % ("Target", list[0], "The Host/IP to attack")
	print "%s \t\t%d \t\t%s\n" % ("Port", list[1], "Port in Host/IP to attack")
	
def scan():
	try:
		line_1 = wcolors.color.UNDERL + wcolors.color.BLUE + "Fploit" + wcolors.color.ENDC
		line_1 += ":"
		line_1 += wcolors.color.UNDERL + wcolors.color.BLUE + "Evil Scan" + wcolors.color.ENDC
		line_1 += " > "
		command = raw_input(line_1)
		
		if command[0:10] == "set target":
			target = command[11:]
			options[0] = target
			print "Target => ", target
			scan()
		elif command[0:8] == "set port":
			port = command[9:]
			options[1] = int(port)
			print "Port => ", port
			scan()
		elif command [0:12] == "show options":
			show_options(options)
			scan()
		elif command [0:4] == "back":
			print "Later!"
			sys.exit()
		elif command [0:3] == "run":
			
			users = ["anonymous","anonymous"+"@"+options[0]]
			passwords = ["guest","anonymous"," ","anonymous"+"@"+options[0]]
	
			print wcolors.color.CYAN + "[*]Wait Please\n" + wcolors.color.ENDC
			for user in users:
				for password in passwords:
					try:
						conect = ftplib.FTP(options[0])
						ans = conect.login(user,password)
						if ans == "230 Login successful.":
							anon_login = "Allowed"
							options.append(anon_login)
						else:
							pass
					except ftplib.error_perm:
						anon_login = "Disallowed"
						options.append(anon_login)
	
			socket.setdefaulttimeout(2)
			s = socket.socket()
			try:
				s.connect((options[0],options[1]))
				ans = s.recv(1024)
				options.append(ans)
				s.close()
			except(socket.error):
				print wcolors.color.RED + "Can't connect" + wcolors.color.ENDC
			
			
			print wcolors.color.CYAN + "IP: " + options[0] + wcolors.color.ENDC
			print wcolors.color.CYAN + "Port: " + str(options[1]) + wcolors.color.ENDC
			print wcolors.color.CYAN + "FTP Banner: " + options[3] + wcolors.color.ENDC
			print wcolors.color.CYAN + "Anonymous Access: " + options[2] + "\n" + wcolors.color.ENDC	
		else:
			print "Unknown"
			scan()		
	except(KeyboardInterrupt):
		print "Interrupted. Later!"
		sys.exit()

scan()
