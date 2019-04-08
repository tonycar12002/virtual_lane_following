# README #

Duckiebot Simulator by Duckietown NCTU
This README would normally document whatever steps are necessary to get your application up and running.
[Duckietown lane following repo](https://github.com/duckietown/Software)

### What is this repository for? ###

* A ros package
* Virtual lane following in gazebo
* Clone this repo to duckietown 

### How do I get set up? ###

1. Install some packages about ros, gazebo, python
```
$ source file_downloads.sh
$ source create_machine.sh
$ bash install_dependency.sh
``` 
 
### How to run the code? ###

1. first terminal:
```
$ cd
$ cd duckietown
$ source environment.sh
$ roslaunch duckiebot_gazebo duckietown_world_mobile_bot.launch 
```
2. second terminal:
```
$ cd
$ cd duckietown
$ source environment.sh
$ roslaunch duckiebot_control gazebo_lane_following.launch
```
3. third terminal:
```
$ cd
$ cd duckietown
$ source environment.sh
$ rviz
```

### Who do I talk to? ###

* Repo owner or admin
