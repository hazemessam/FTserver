# FTP Server
FTP server streams my media files from my PC to my WLAN devices.

## Tech Stack
- Python
- Flask
- Docker
- Nginx

## Setup

#### 1. Clone the repo.
```bach
git clone https://github.com/hazemessam/ftp-server.git
```

#### 2. Enter the project directory.
```bash
cd ftp-server
```
#### 3. Set the `MEDIA_DIR` environment variable to your media directory path (add it to the `.env` file for consistency).
```bash
export MEDIA_DIR=<path/to/media/dir>
```

#### 4. Build the project using docker compose.
```bash
docker compose build
```


#### 5. Run the project using docker compose.
```bash
docker compose up
```

#### 6. Now check the service runing on the port `80` form your PC http://localhost/.

#### 7. Open the port `80` on your PC to be able to access the service from your WLAN devices.

#### 8. Set a static IP address to your PC using your DHCP server then use this IP to access the service from your WLAN devices (ex. http://192.168.1.2/).
