# Autonomous Drone Navigation

## System
PX4 SITL + Gazebo
Ubuntu 20.04

## Build
docker build -t drone .

## Run
docker run drone

## Mission Flow
IDLE → TAKEOFF → SEARCH → DESCEND → SCAN → LAND

## Control Mode
OFFBOARD

## Logs
PX4 .ulg logs recorded at 10Hz

## Perception
OpenCV ArUco detection

## Navigation
Dead reckoning + odometry
