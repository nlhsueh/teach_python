# 08_tcp_chat_client.py - 多用戶 TCP Socket 聊天室用戶端

import socket
import threading
import sys

def receive_messages(client_socket):
    """ 背景執行緒：持續接收來自伺服器的廣播訊息 """
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                print("\n[系統] 與伺服器的連線已中斷。")
                break
            print(f"\n{message}", end="")
            print("[發言] > ", end="", flush=True)
        except Exception:
            break

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(('127.0.0.1', 8080))
        
        # 啟動接收背景執行緒
        recv_thread = threading.Thread(target=receive_messages, args=(client_socket,))
        recv_thread.daemon = True
        recv_thread.start()
        
        print("已成功連線至聊天伺服器。輸入訊息並按 Enter 送出，輸入 'exit' 可離開。")
        while True:
            msg = input("[發言] > ")
            if msg.lower() == 'exit':
                break
            if msg.strip():
                client_socket.send(msg.encode('utf-8'))
    except ConnectionRefusedError:
        print("[錯誤] 連線失敗：伺服器未啟動 (請先執行 07_tcp_chat_server.py)")
    except Exception as e:
        print(f"[錯誤] 發生異常：{e}")
    finally:
        client_socket.close()
        print("已退出聊天室。")

if __name__ == '__main__':
    start_client()
