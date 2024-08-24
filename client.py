import socket

HOST = 'localhost'
PORT = 65432  # サーバーと同じポート番号
BUFFER_SIZE = 4096

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    try:
        client_socket.connect((HOST, PORT))
        print(f"サーバ{HOST}:{PORT}に接続しました。")
    except ConnectionRefusedError:
        print(f"{HOST}:{PORT}に接続できませんでした。サーバが起動していることを確認してください。")
        exit(1)

    try:
        while True:
            message = input("サーバに送信するメッセージを入力してください ('end'で終了): ")
            if message.lower() == 'end':
                client_socket.sendall('end'.encode('utf-8'))
                break

            if message:  # 空文字列でない場合のみ送信
                client_socket.sendall(message.encode('utf-8'))
                data = client_socket.recv(BUFFER_SIZE)
                if not data:
                    print("サーバから切断されました。")
                    break
                print(f"サーバからの応答: {data.decode('utf-8')}")

    except socket.error as e:
        print(f"通信エラーが発生しました: {e}")
    finally:
        client_socket.close()