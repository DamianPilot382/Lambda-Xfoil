# XFOIL-Server

Build the image with

```bash
docker build -t XFOIL-Server .
```

Run the Docker container with:

```bash
docker run -p 5000:5000 XFOIL-Server
```

or both with:
```bash
docker build -t xfoil-web . && docker run -p 3000:3000 xfoil-web
```

Access at:
http://127.0.0.1:5000
