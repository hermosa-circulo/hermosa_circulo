夢のある研究
====

#Overview  
男達はグランドラインを目指し、夢を追い続ける。世は正に大海賊時代！  

## Description
3DモデルをIGAで最適化  
djangoを使って書いてます([使いかた](http://docs.djangoproject.jp/en/latest/intro/tutorial01.html))  

## フォルダ構成
###app
---
webアプリ本体  
####/views.py
httpリクエストを受けてレスポンスを返す処理を書くファイル  
####/utils
3Dモデリングの更新に使っている関数をとりあえずこの中に入れた  
####/templates
webアプリで使うhtmlテンプレート  
####/static
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
    python 2.7 or 3.4  
## How to Use(local)
    $git clone https://github.com/m-masataka/oppai_iga.git  
    $cd oppai_iga  
    $pip install -r requirements.txt  
    $python manage.py migrate  
    $python manage.py runserver  
Now, you can access [http://localhost:8000/boobs_designer/](http://localhost:8000/boobs_designer/)  
## How to Deploy
Centos7を前提としたコマンド

    $git clone https://github.com/m-masataka/oppai_iga.git  
    $cd oppai_iga  
    $yum groupinstall -y "development tools"  
    $yum install -y python-devel　mod_wsgi  
    $後はmod_wsgiの設定とhttpdの再起動とファイアウォールの設定をして完了  
## Author
[m-masataka](https://github.com/m-masataka)  
[bandoshintaro](https://github.com/bandoshintaro)  
