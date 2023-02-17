# RoboBoat (now with ROS)

## Setting up your Development Environment (DE)

### Installing Docker

Please refer to the [docker setup tutorial ](https://github.com/MHSeals/Docker-Tutorial/blob/main/Docker/setup.md)to get Docker set up on your device.

### Pull the Docker Image

```console
mhseals@roboboat:~$ docker pull mhseals/roboboat-2022
```

### Clone the Repository

```console
mhseals@roboboat:~$ git clone https://github.com/MHSeals/roboboat-2022
```

### Install the VSCode Extensions (optional, but recommended)
If you use VSCode, 
- install the `Dev Containers` extension
- Run your docker image
    - `./docker-run.sh` on Linux
    - Just run the image using `Docker Desktop` on Windows
- VSCode command `Dev Containers: Attach to Running Container` to open a new window with the container

### NeoVim Plugin Extension
If you use NeoVim, I found this pretty rad [extension](https://github.com/jamestthompson3/nvim-remote-containers) that allows you to attach to a container.