## Docker configuration file for the Turbinia client
This Docker configuration is for building Turbinia client image.

### Build the image
```
docker build -t turbinia-client .
```

### Turbinia configuration
The Turbinia configuration file needs to be mapped into the container for the client tool to pickup the correct settings. You can use a file volume mapping to achieve this. See [here](https://raw.githubusercontent.com/google/turbinia/master/turbinia/config/turbinia_config_tmpl.py) for an example configuration file.

### Run the client
```
docker run -ti \
-v $(PWD)/.turbiniarc:/etc/turbinia/turbinia.conf \
turbinia-client -h
```
