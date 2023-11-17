from setuptools import setup

package_name = 'my_ros_chatbot_package'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your_email@example.com',
    description='ROS Chatbot for Service Robot',
    license='LICENSE',
)

