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

![client接続](https://user-images.githubusercontent.com/50327128/111060908-aaa03200-84e3-11eb-8832-0e72f2e28b74.JPG)

2. アップロード

![clientアップロード0](https://user-images.githubusercontent.com/50327128/111060909-ac69f580-84e3-11eb-89a7-c72e6abfdfa3.JPG)
![clientアップロード1](https://user-images.githubusercontent.com/50327128/111060911-ae33b900-84e3-11eb-8cd4-124632410b89.JPG)

3. サーバー側のファイルリストをチェック

![clientファイルリスト](https://user-images.githubusercontent.com/50327128/111060915-b4299a00-84e3-11eb-9da2-9f4b8044fc4d.JPG)

4. ダウンロード

![clientダウンロード](https://user-images.githubusercontent.com/50327128/111060917-b7bd2100-84e3-11eb-842f-bf29282be6de.JPG)
![clientダウンロード1](https://user-images.githubusercontent.com/50327128/111060919-b8ee4e00-84e3-11eb-840f-36abceae4aac.JPG)

5. 終了

![client-exit](https://user-images.githubusercontent.com/50327128/107136952-132b4a80-694b-11eb-9c17-95b40eb8f2c3.JPG)
