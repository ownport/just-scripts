# Working with docker images

`docker-images.sh` shell script helps import docker images to archive file and pull (export) them to docker registry

## How to use

### Import docker images to archive

```sh
./docker-images.sh import -l <docker images list> -i <tar.gz archive with docker images>
```
Example:
```sh
./docker-images.sh import -l samples/rancher-images.v2.3.3.list -i rancher-images.v2.3.3.tar.gz
```

### Export docker images from archive file to registry

to be described later


