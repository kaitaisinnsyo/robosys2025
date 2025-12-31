from setuptools import find_packages, setup

package_name = 'robosys2025'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shibu0907',
    maintainer_email='mdouga0907@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'cpu_publisher = robosys2025.cpu_publisher:main',
            'load_alert = robosys2025.load_alert:main',
        ],
    },
)
