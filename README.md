# Roboboat (now with ROS)

## Setting up your Development Environment (DE)

### Installing ROS

Follow the [ROS Noetic Installation Guide](http://wiki.ros.org/noetic/Installation/Ubuntu). Or, td;lr copy-paste and run:

```console
user@host:~$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
user@host:~$ curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
user@host:~$ sudo apt update
user@host:~$ sudo apt install ros-noetic-desktop-full
user@host:~$ sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool python3-catkin-tools build-essential
user@host:~$ sudo rosdep init
user@host:~$ rosdep update
user@host:~$ echo "\nsource /opt/ros/noetic/setup.bash" >> ~/.bashrc    # or .zsh >> ~/.zshrc if you're using zsh, etc.
```

### Cloning the Repository

> :warning: When ROS build your package, it will spawn `build/` and `devel/`. You may want to clone into an isolated workspace folder e.g `Workspace` or `catkin_ws` (a ROS naming convention).

```console
user@host:~$ git clone git@github.com:MHSeals/roboboat-2022.git catkin_ws
user@host:~$ cd catkin_ws
user@host:~$ catkin build
[a bunch of build message, should all succeed]
user@host:~$ echo "\nsource /home/user/catkin_ws/devel/setup.bash"  # IMPORTANT!
```

Be sure to double check your .bashrc files to see if everything is pointing to the correct `setup.bash` file. This is essential for ROS to find your package and allow using ROS commands e.g. `roscd`, `roslaunch`, `rosrun`, etc.

## Run example code

At this point, you should be able to launch ROS from anywhere. Our package is named `roboboat_ros`, so our standard script calling looks like this

```console
user@host:~$ roslaunch roboboat_ros start_velodyne_backend.launch show_rviz:=true
```

This will launch multiple things, have a look at [ROS Launch XML Syntax](http://wiki.ros.org/roslaunch/XML).

To run a single node to serve some purpose (e.g. display pointcloud data in Python TKinter), use singular run instead of launch:

```console
user@host:~$ rosrun roboboat_ros read_velodyne_data.py
```

The [`read_velodyne_data.py`](./src/roboboat_ros/scripts/read_velodyne_data.py) script is a small, simple example covering a number of essential ROS topics, such as publisher, subscriber, callback functions, and ROS node handling.