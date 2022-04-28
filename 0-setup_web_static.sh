#!/usr/bin/env bash
sudo apt-get update
sudo apt-get install nginx -y
sudo mkdir /data/
sudo mkdir /data/web_static/
sudo mkdir /data/web_static/releases/
sudo mkdir /data/web_static/shared/
sudo mkdir /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
echo '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>' > /data/web_static/releases/test/index.html
sudo rm -rf /data/web_static/current
sudo ln -s /data/web_static/current /data/web_static/releases/test/
sudo chown -hR ubuntu:ubuntu /data/
sudo cp -r /data/web_static/current/* /data/web_static/$1
sudo service nginx restart
