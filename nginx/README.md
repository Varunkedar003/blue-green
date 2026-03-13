Nginx Load Balancer Configuration

This project uses Nginx as a reverse proxy and load balancer to route user traffic to either the Blue or Green environment.

Purpose

Nginx is used to:

Route traffic to the active environment

Enable Blue-Green deployment switching

Act as a reverse proxy for the Flask application

Configuration File

Location on server:

/etc/nginx/sites-available/app.conf

Enable configuration:

sudo ln -sf /etc/nginx/sites-available/app.conf /etc/nginx/sites-enabled/default

Reload nginx after switching traffic:

sudo systemctl reload nginx
Blue-Green Traffic Switching

Blue Environment

server 15.206.149.116:5000;

Green Environment

server 65.0.19.164:5000;

Jenkins pipeline automatically modifies the upstream server during deployment.
