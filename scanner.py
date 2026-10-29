import socket

target = <"ip">

def check_port(port):
    s = socket.socket()
    s.settimeout(1)
    result = s.connect_ex((target, port))
    s.close()
    return result == 0

print("Scanning", target)
for port in range(1, 101):
    if check_port(port):
        print("Port", port, "is OPEN")
print("Done")
