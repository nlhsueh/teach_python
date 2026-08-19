# 07_tcp_chat_server.py - 多用戶 TCP Socket 聊天室伺服器 (多執行緒架構)

import socket
import threading

HOST = '127.0.0.1'
PORT = 8080
clients = []  # 儲存所有已連線用戶端的 socket 物件

def broadcast(message, sender_client):
    """ 將訊息廣播給除了發送者之外的所有人 """
    for client in clients[:]:
        if client != sender_client:
            try:
                client.send(message)
            except Exception:
                client.close()
                if client in clients:
                    clients.remove(client)

def handle_client(client_socket, client_address):
    """ 背景處理每一個單獨的用戶端連線 """
    print(f"[新連線] 用戶進入：{client_address}")
    try:
        client_socket.send("歡迎加入 TCP 聊天室！請開始發言。\n".encode('utf-8'))
        
        while True:
            message = client_socket.recv(1024)
            if not message:
                break
            
            decoded = message.decode('utf-8').strip()
            print(f"[訊息] 用戶 {client_address[1]}: {decoded}")
            
            # 廣播給其他在線用戶
            broadcast(f"用戶 {client_address[1]} 說: {decoded}\n".encode('utf-8'), client_socket)
    except Exception as e:
        print(f"[異常] 用戶 {client_address} 連線中斷: {e}")
    finally:
        print(f"[斷開] 用戶離線：{client_address}")
        if client_socket in clients:
            clients.remove(client_socket)
        client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 設置 SO_REUSEADDR 避免 TIME_WAIT 導致 Address already in use
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"[啟動] TCP 聊天伺服器已在 {HOST}:{PORT} 監聽連線...")
    print("等待用戶端連線中 (按 Ctrl+C 可關閉伺服器)...")

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            clients.append(client_socket)
            
            # 為新連線建立獨立的背景工作執行緒
            thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            thread.daemon = True
            thread.start()
    except KeyboardInterrupt:
        print("\n[關閉] 伺服器正在安全關閉...")
    finally:
        server_socket.close()

if __name__ == '__main__':
    start_server()
