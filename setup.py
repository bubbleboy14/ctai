from setuptools import setup

setup(
    name='ctai',
    version="0.1",
    author='Mario Balibrera',
    author_email='mario.balibrera@gmail.com',
    license='MIT License',
    description='AI plugin for cantools (ct)',
    long_description='This plugin combines aiio models and functionality with the cantools bot system.',
    packages=[
        'ctai'
    ],
    zip_safe = False,
    install_requires = [
        "aiio >= 0.1"
    ],
    entry_points = '''''',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
