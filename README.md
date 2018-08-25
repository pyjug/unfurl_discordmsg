
# 環境設定

1. 次のURLを参考に、Google Cloud Datastore のキーファイルを作成する

    https://cloud.google.com/datastore/docs/reference/libraries


2. Discord bot のトークンを、任意のファイルに保存する

     ex)
         $ echo asdf89as9d8fndfssa8.asfasf98f7isaidfuhasf > $HOME/mybottoken

3. 作成したDiscord bot トークンファイルのファイル名を、次のように環境変数に指定する


    export DISCORD_BOT_KEYFILE="[KEY]"

    ex)
        export DISCORD_BOT_KEYFILE="%HOME/mybottoken"

4. 実行環境を作成する

```
$ pip install pipenv
$ git clone https://github.com/pyjug/unfurl_discordmsg.git
$ unfurl_discordmsg
$ pipenv install --three
```

5. 実行する


```
$ pipenv run python -m unfurl_discordmsg
```

Permissions:
View channels
Send Message
Embed Links
Read Message History
