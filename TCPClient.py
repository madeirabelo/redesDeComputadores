from socket import *
import sys
serverName = '127.0.0.1'
serverPort = 80
try:
    clientSocket = socket(AF_INET, SOCK_STREAM) 
    print ("Socket successfully created")
    clientSocket.connect((serverName,serverPort))
    request     = "GET /dashboard/ HTTP/1.1\r\nHost:%s\r\n\r\n" % serverName
    clientSocket.send(request.encode())
    webServer = clientSocket.recv(32768) 
    print(webServer.decode()) 
    clientSocket.close()
except OSError as err:
    sys.exit("Socket Failed with Error %s" %(err))



#Hypertext Transfer Protocol
#    GET /dashboard/ HTTP/1.1\r\n
#        [Expert Info (Chat/Sequence): GET /dashboard/ HTTP/1.1\r\n]
#        Request Method: GET
#        Request URI: /dashboard/
#        Request Version: HTTP/1.1
#    Host: 127.0.0.1\r\n
#    Upgrade-Insecure-Requests: 1\r\n
#    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n
#    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15\r\n
#    Accept-Language: en-us\r\n
#    Accept-Encoding: gzip, deflate\r\n
#    Connection: keep-alive\r\n
#    \r\n
#    [Full request URI: http://127.0.0.1/dashboard/]
#    [HTTP request 1/1]
#    [Response in frame: 7]


