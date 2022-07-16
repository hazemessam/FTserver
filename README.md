# FTP Server
FTP server streams media files from my PC to my iPhone using my local WLAN.

# Setup

#### 1. Clone the repo
```bach
git clone https://github.com/hazemessam/ftp-server.git
```

#### 2. Enter the project directory
```bash
cd ftp-server
```

#### 3. Build the docker image
```bash
docker build -t ftp-server .
```

#### 4. Set `MEDIA_DIR` variable to your media directory path
```bash
MEDIA_DIR=<path/to/media/dir>
```

#### 5. Run the docker container
```bash
docker run -d -v $MEDIA_DIR:/app/media -p 2121:8080 --name ftp-server ftp-server
```

#### 6. Set a static IP address to your PC using your DHCP server then use this IP to access the FTP server on port `2121` (ex. http://192.168.1.2:2121/).
