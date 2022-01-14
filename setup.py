from setuptools import setup

package_name = 'led_control_python'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='plantstoen',
    maintainer_email='plantstoen@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'led_control_server = led_control_python.led_control_server_v1:main',
            'led_control_client = led_control_python.led_control_client_v1:main',
        ],
    },
)
