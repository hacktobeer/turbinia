## Docker configuration file for the Turbinia API server

This Docker configuration is for building Turbinia API server images.

### Build the image

```
docker build -t turbinia-api-server:dev -f docker/api-server/Dockerfile .
```

### Run the worker

Make sure you have a correctly configuration `turbinia.conf` file for your environment.

```
docker run -ti \
-v $PWD/turbinia.conf:/etc/turbinia/turbinia.conf \
turbinia-api-server:dev
```
