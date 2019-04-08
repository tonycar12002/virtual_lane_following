#!/bin/bash
sudo rm -rf /var/lib/dpkg/lock
#duckiefleet
file="$HOME/duckiefleet"
if [ -d "$file" ]
then
	echo "$file already exist"
else
	echo "Clone $file"
	cd 
	git clone https://github.com/tonycar12002/duckiefleet.git duckiefleet
fi

#duckietown
file="$HOME/duckietown"
if [ -d "$file" ]
then
	echo "$file already exist"
else
	echo "Clone $file"
	cd 
	git clone https://github.com/duckietown/Software.git duckietown
fi

#virtual lane following
file="$HOME/duckietown/catkin_ws/src/virtual_lane_following"
if [ -d "$file" ]
then
	echo "$file already exist"
else
	echo "Clone $file"
	cd 
	git clone https://github.com/tonycar12002/virtual_lane_following.git
	mv $HOME/virtual_lane_following/ $HOME/duckietown/catkin_ws/src/
fi
cd $HOME/duckietown/catkin_ws/src/virtual_lane_following/
bash install_dependency.sh

cd $HOME/duckietown/catkin_ws
catkin_make
