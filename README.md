夢のある研究
====

#Overview  
男達はグランドラインを目指し、夢を追い続ける。世は正に大海賊時代！  

## Description
3DモデルをIGAで最適化  
djangoを使って書いてます([使いかた](http://docs.djangoproject.jp/en/latest/intro/tutorial01.html))  

## フォルダ構成
- app webアプリ本体  
    - /views.py  httpリクエストを受けてレスポンスを返す処理を書くファイル  
    - /utils  3Dモデリングの更新に使っている関数をとりあえずこの中に入れた  
    - /templates  webアプリで使うhtmlテンプレート  
    - /static  webアプリで使う静的ファイル  
- oppai_iga django  プロジェクト全体の設定ファイルがおいてある  
- templates django  プロジェクト全体で使うhtmlテンプレート  
- static django  プロジェクト全体で使う静的ファイル  
## Requirement
    python 2.7  
## How to Use(local)
    $git clone https://github.com/m-masataka/oppai_iga.git  
    $cd oppai_iga  
    $pip install -r requirements.txt  
    $python manage.py migrate  
    $python manage.py runserver  
Now, you can access [http://localhost:8000/boobs_designer/](http://localhost:8000/boobs_designer/)  
## How to Deploy
Centos7を前提としたコマンド

言語設定

    $sudo localectl set-locale LANG=ja_JP.UTF-8

必要なライブラリをインストール  

    $sudo yum update -y
    $sudo yum install -y epel-release
    $sudo yum install -y groupinstall 'Development tools'
    $sudo yum install -y git python-devel httpd-devel openldap-devel

httpdとwsgiのインストール

    $sudo yum install -y httpd mod_wsgi

mod_wsgiの設定ファイルを作成  

    $sudo sh -c "cat << '_EOT_' > /etc/httpd/conf.modules.d/10-wsgi.conf
    LoadModule wsgi_module modules/mod_wsgi.so

    WSGIScriptAlias / /var/service/oppai_iga/oppai_iga/wsgi.py
    WSGIDaemonProcess oppai_iga user=apache group=apache python-path=/var/service/oppai_iga:/usr/lib/python2.7/site-packages
    WSGIProcessGroup oppai_iga
    WSGISocketPrefix run/wsgi
    Alias /static/ /var/service/oppai_iga/static/

    <Directory /var/service/oppai_iga/oppai_iga>
        <Files wsgi.py>
            <IfVersion < 2.4>
                Allow from all
            </IfVersion>
            <IfVersion >= 2.4>
                Require all granted
            </IfVersion>
        </Files>
    </Directory>

    <Directory /var/service/oppai_iga/static>
        <IfVersion < 2.4>
            Allow from all
        </IfVersion>
        <IfVersion >= 2.4>
            Require all granted
        </IfVersion>
    </Directory>
    _EOT_"

プログラムのソースコードをgit clone  

    $sudo mkdir /var/service
    $sudo git clone https://github.com/m-masataka/oppai_iga.git /var/service/oppai_iga

権限を設定

    $sudo chown apache:apache /var/service/oppai_iga -R

SELinuxを無効化

    $setenforce 0

/etc/selinux/configの記述を変更

    SELINUX=disabled

pipおよびpythonのライブラリをインストール  

    $sudo yum install -y python-pip && sudo pip install pip --upgrade
    $sudo pip install -r /var/service/oppai_iga/requirements.txt

firewalldのhttp,httpsのポートを開ける  

    $sudo firewall-cmd --add-service=http --zone=public --permanent
    $sudo firewall-cmd --add-service=https --zone=public --permanent
    $sudo systemctl restart firewalld
    $sudo systemctl enable firewalld

httpdを有効化  

    $sudo systemctl restart httpd
    $sudo systemctl enable httpd

Blenderで３Ｄモデルを操作するために"blender"をインストールしてください

    $yum install blender

## Author
[m-masataka](https://github.com/m-masataka)  
[bandoshintaro](https://github.com/bandoshintaro)  
