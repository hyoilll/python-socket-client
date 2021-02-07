# Python ソケット通信を利用したファイルを伝送するプログラム

---

**概要**

- クライアント側からサーバー側までファイルを伝送し、セーブするプログラム

**作業期間**

- 一週間

**開発言語・技術：**

- Python

**分類**

1. チェット

2. ファイル伝送

**機能**

1. チェット
   - Thread を利用してリアルタイムでクライアント側とサーバー側が通信することが可能
2. ファイル伝送
   - クライアント側からサーバー側までアップロード
   - サーバー側からクライアント側までダウンロード
   - サーバー側のファイルリストをチェック

**シミュレーション**

1. 接続

![client-connect](https://user-images.githubusercontent.com/50327128/107136923-dd866180-694a-11eb-927d-fccc5f1261ae.JPG)

2. アップロード

![client-upload](https://user-images.githubusercontent.com/50327128/107136930-f55de580-694a-11eb-9570-7cb8e936002a.JPG)

3. サーバー側のファイルリストをチェック

![client-filelistprint](https://user-images.githubusercontent.com/50327128/107136936-fd1d8a00-694a-11eb-9242-dd92ea3e2872.JPG)

4. ダウンロード

![client-download](https://user-images.githubusercontent.com/50327128/107136942-06a6f200-694b-11eb-9238-00984448aece.JPG)
![client-download2](https://user-images.githubusercontent.com/50327128/107136950-0d356980-694b-11eb-80a9-d0d88adb4f06.JPG)

5. 終了

![client-exit](https://user-images.githubusercontent.com/50327128/107136952-132b4a80-694b-11eb-9c17-95b40eb8f2c3.JPG)
