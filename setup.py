from setuptools import setup

setup(
    name='autogmailpy',
    version='0.1',
    packages=['autogmailpy'],
    url='https://github.com/izaac/autogmailpy',
    license='MIT',
    author='Izaac Zavaleta',
    author_email='jorge.izaac@gmail.com',
    description='Python Selenium Gmail Tests',
    test_suite='autogmailpy.tests',
    install_requires=['selenium>=2.44.0'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
