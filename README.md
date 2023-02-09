# README

1. [新增專案 – Google Cloud Console](https://console.cloud.google.com/projectcreate?previousPage=%2Fapis%2Fcredentials%3Fproject%3Dkinetic-bot-367806&organizationId=0)
2. 選取專案
3. `+建立憑證` -> `OAuth 用戶端ID` -> `設定同意畫面` 
4. `OAuth` -> `電腦版應用程式` -> 命名 -> 下載json
5. `測式使用者` -> `+ ADD user` -> `輸入信箱(一定要是google)`
6. 將json命名為`credentials.json` -> `放入專案中`
7. `pip install -r requirements.txt` 
8. edit `title.html`, `content.html`
8. run `python send-mail`
