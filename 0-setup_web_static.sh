#!/usr/bin/env bash
# Prepare your web servers
sudo apt-get update
sudo apt-get install nginx -y
sudo mkdir -p /data/web_static/shared/ /data/web_static/releases/test/

echo '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>' > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sed -i "58i \\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-enabled/default
sudo service nginx restart
exit 0
