cmake_minimum_required(VERSION 2.8.3)
project(concert_software_common)

find_package(catkin REQUIRED)

catkin_package()

install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})

install(DIRECTORY software
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
