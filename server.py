import socket
import threading
from faker import Faker

HOST = 'localhost'
PORT = 65432
MAX_CLIENTS = 5
BUFFER_SIZE = 4096

faker = Faker()

def handle_client_connection(client_socket, address):
    try:
        print(f"クライアント{address}から接続されました。")
        while True:
            data = client_socket.recv(BUFFER_SIZE)
            if not data:
                break  # データがない場合はクライアントが接続を閉じたと判断

            received_message = data.decode('utf-8')
            print(f"クライアントからのメッセージ: {received_message}")

            # クライアントからのメッセージが "end" なら接続を閉じる
            if received_message.lower() == "end":
                client_socket.sendall("接続を終了します。".encode('utf-8'))
                break
            
            fake_data = faker.text()

            client_socket.sendall(fake_data.encode('utf-8'))

    except socket.error as e:
        print(f"ソケットエラー: {e}")
    finally:
        client_socket.close()
        print(f"クライアント{address}との接続を終了します。")

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(MAX_CLIENTS)
        print(f"サーバは{HOST}:{PORT}で起動しています。")

        try:
            while True:
                client_socket, address = server_socket.accept()
                client_thread = threading.Thread(target=handle_client_connection, args=(client_socket, address))
                client_thread.start()
        except KeyboardInterrupt:
            print("サーバーがキーボード入力によって終了しました。")

# サーバー起動
start_server()