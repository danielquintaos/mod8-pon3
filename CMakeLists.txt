cmake_minimum_required(VERSION 3.5)
project(my_ros_chatbot_package)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)

# Uncomment if the package has executable scripts in the 'scripts' folder
# install(PROGRAMS
#   scripts/chatbot_node.py
#   DESTINATION lib/${PROJECT_NAME}
# )

ament_package()

