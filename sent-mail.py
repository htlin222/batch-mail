#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# title: sent-mail
# date: "2023-02-09"
import yagmail
import pandas as pd
from email.mime.text import MIMEText


sent_from = "ppoiu87@gmail.com"


def main():

    file = ['報名表.docx']  # 傳送多個檔案 以list型態
    df = pd.read_excel("file.xlsx")
    email_addresses = df["email"].tolist()
    names = df["name"].tolist()

    with open('content.html', encoding='utf8') as f:
        # content_tempate='\n'.join(f.readlines())
        content_tempate = f.read()

    with open('title.html', encoding='utf8') as f:
        # content_tempate='\n'.join(f.readlines())
        title_tempate = f.read()

    for index, email_address \
            in enumerate(email_addresses):
        print(f"第{index+1}封信，即將寄給{names[index]}")
        title = names[index] + title_tempate
        content = names[index] + content_tempate
        yag = yagmail.SMTP(sent_from,
                           oauth2_file="credentials.json")
        print("...處理中...")
        yag.send(
            to=email_address,
            subject=title,
            contents=content,
            attachments=file
        )

        print("信已寄出")

if __name__ == '__main__':
    main()
    print("Done 🟢")

