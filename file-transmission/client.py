from socket import *
import os
import sys

clientSock = socket(AF_INET, SOCK_STREAM)

# HOST = 'ec2-3-36-58-88.ap-northeast-2.compute.amazonaws.com'
# PORT = 9000

HOST = '127.0.0.1'
PORT = 8080

clientSock.connect((HOST, PORT))
print('サーバー側に接続しました。')

while True:
    print('# 1 クライアント -> サーバー アップロード')
    print('# 2 サーバー -> クライアント ダウンロード')
    print('# 3 サーバー側のファイルリストをチェック')
    print('exit -> 999')
    print('menu -> ', end='')
    menu = int(input())

    if menu == 1:  # 1 クライアント -> サーバー ファイルをアップロード
        menu = str(menu)
        clientSock.send(menu.encode('utf-8'))

        while True:
            data_transferred = 0
            fileName = input('伝送するファイルのタイトルを入力してください。 :')

            # 今のディレクトリーの中にファイルがあるかどうかチェック
            path_dir = os.getcwd()
            file_list = os.listdir(path_dir)

            # ありましたら伝送
            if fileName in file_list:
                # filename 伝送
                clientSock.send(fileName.encode('utf-8'))

                print('ファイル : %s / 伝送スタット' % fileName)

                with open(fileName, 'rb') as f:
                    try:
                        data = f.read(1024)
                        while data:
                            data_transferred += clientSock.send(data)
                            data = f.read(1024)
                    except Exception as ex:
                        print(ex)

                print('伝送完了 %s, 伝送量 %d' % (fileName, data_transferred))
                break
            # ファイルが存在してないので、もう一度入力
            else:
                print('今のディレクトリーにはファイルがありません。')
    elif menu == 2:  # 2 サーバー -> クライアント ファイルをダウンロード
        menu = str(menu)
        clientSock.send(menu.encode('utf-8'))

        fileName = input('ダウンロードするファイルのタイトルを入力してください。: ')
        clientSock.send(fileName.encode('utf-8'))

        data = clientSock.recv(1024)
        data_transferred = 0

        if data.decode('utf-8') == 'Nothing File':
            print('ファイル %s がサーバーに存在しておりません。' % fileName)
        else:
            nowdir = os.getcwd()
            print('path : ', nowdir)

            # 今のディレクトリーにファイルをセーブする
            with open(nowdir + '\\' + fileName, "wb") as f:
                print('hello1')
                try:
                    print('hello2')
                    while data:  # 　データがある時まで
                        print('hello3')
                        f.write(data)  # 1024バイトを書く
                        print('hello4')
                        data_transferred += len(data)
                        print(data_transferred)

                        # 1024より少ないとことは次のデータがないということを意味する
                        if len(data) < 1024:
                            break

                        data = clientSock.recv(1024)   # 1024バイトを貰う
                except Exception as ex:
                    print(ex)

            print('受信完了 %s, 伝送量 %d' % (fileName, data_transferred))
    elif menu == 3:  # 3 サーバー側のファイルリストチェック
        menu = str(menu)
        clientSock.send(menu.encode('utf-8'))

        file_list = clientSock.recv(1024)
        file_list = file_list.decode('utf-8')
        print('server file-list : ', file_list)
    elif menu == 999:
        break
    else:
        print('1 ~ 3の範囲で選んでください。')

clientSock.close()
