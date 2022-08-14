import socket, time, os 


HOST = '0.0.0.0'                 # Symbolic name meaning all available interfaces
PORT = int(os.environ.get('PORT'))              # Arbitrary non-privileged port
VERSION = os.environ.get('VERSION')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            # data = conn.recv(1024)
            # if not data: break
            data = f"VERS: {VERSION} connected from: {addr}\n"
            conn.sendall(data.encode())
            time.sleep(1)