import socket
from pythonping import ping

# founction to get ping response
def rep(ip):
    response = ping(ip,count=1,timeout=0.5,verbose=False)  
    # Convert response to binary: 1 if reachable, 0 if not
    binary_response = 1 if response.success() else 0
    return binary_response



hostname = socket.gethostname()
ip_a= socket.gethostbyname(hostname)
print("hostname",hostname)
print("ip adrr",ip_a)#getting local ip


# ip_a =ip_a.rsplit('.',1)[0]#getting net id 
print("net id",ip_a)


#iterating through all possible host id s
for i in range(1,255):
    ip_a = ip_a.rsplit(".",1)[0] #spliting the net id and host id and saving net id
    ip_a += "."+str(i) #adding the ith host id
    print(ip_a,"-->",rep(ip_a))
print("completed")
    
