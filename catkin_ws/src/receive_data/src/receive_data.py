import socket, traceback

def setupSocket():
    host = '172.16.100.143'
    port = 5555
 
    global s 
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.bind((host, port))

    print "setup finish@@@"

def revceiveImuData():
    try:
        message, address = s.recvfrom(8192)
        #print (message)
	return message
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()
