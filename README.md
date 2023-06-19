This is a Sample Python Server Application that uses the Flask framework.

## Installation

Create and activate a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install required Python packages:

```bash
pip install -r requirements.txt
```

## Running the application

if you want the application to run on https, you need to have a certificate and key file.

```bash
echo "-----BEGIN CERTIFICATE-----
<paste the certificate content here>
-----END CERTIFICATE-----" > certificate.crt
```

```bash
echo "-----BEGIN PRIVATE KEY-----
<paste the certificate content here>
-----END PRIVATE KEY-----" > privatekey.key
```

Convert to pem format

```bash
openssl x509 -in certificate.crt -out certificate.pem -outform PEM
```

```bash
openssl rsa -in privatekey.key -out privatekey.pem -outform PEM
```

Start the API server using Gunicorn:

```bash
gunicorn --bind 0.0.0.0:5000 --certfile=path/to/ssl_cert.pem --keyfile=path/to/ssl_key.pem <python-script>:app

```

Configure your server's firewall to allow incoming connections on port 5000. For example, using UFW:

```bash
sudo ufw allow 5000
```

Access your API via HTTPS using the following URL format:

```bash
https://<your-server-ip>:5000
```

## Running the application as a service

*** Stop the application if it is running

To run the application as a service, you need to create a service file.

```bash
sudo nano /etc/systemd/system/api.service
```

```bash
[Unit]
Description=API Service
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/<project-directory>
ExecStart=/home/ubuntu/<project-directory>/venv/bin/gunicorn --bind 0.0.0.0:5000 --certfile=/path/to/ssl_cert.pem --keyfile=/path/to/ssl_key.pem app:app
Restart=always

[Install]
WantedBy=multi-user.target
```

Start the service

```bash
sudo systemctl start api
```

Enable the service to start on boot

```bash
sudo systemctl enable api
```

Check the status of the service

```bash
sudo systemctl status api
```

Stop the service

```bash
sudo systemctl stop api
```

Disable the service

```bash
sudo systemctl disable api
```
