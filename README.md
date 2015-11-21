人類が生み出した神をも恐れぬ研究
====

#Overview  
男達はグランドライン(意味深)を目指し、夢を追い続ける。世は正に大海賊時代！  

## Description
3DモデルをIGAで最適化  
探せ！この世の全てをそこにおいてきた！ by 海賊王  

## フォルダ構成
###app
---
webアプリ本体    
####views.py
httpリクエストを受けてレスポンスを返す処理を書くファイル  
####utils
3Dモデリングの更新に使っている関数をとりあえずこの中に入れた  
####templates
webアプリで使うhtmlテンプレート  
####static
webアプリで使う静的ファイル  
###oppai_iga
---
djangoプロジェクト全体の設定ファイルがおいてある  
###templates
---
djangoプロジェクト全体で使うhtmlテンプレート  
###static
---
djangoプロジェクト全体で使う静的ファイル  
## Requirement
    python 2.7, 3.4  

## Install librarys
依存しているライブラリを一括でインストール  

    git clone https://github.com/m-masataka/oppai_iga.git  
    cd oppai_iga  
    pip install -r requirements.txt  

## update requirements.txt
依存しているライブラリの情報を更新  

    pip install pip-tools  
    pip-compile requirements.in  

## Author
[m-masataka](https://github.com/m-masataka)  
[bandoshintaro](https://github.com/bandoshintaro)
