from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as fh:
    readme = fh.read()

setup(
    name='metamorproxies',
    version='0.3.10.6',
    url='https://github.com/reinanbr/metamorproxies',
    license='MIT License',
    author='Reinan Br',
    author_email='slimchatuba@gmail.com',
    description=u'Library for working wih proxies',
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords='proxies',
    packages=find_packages(),
    install_requires=[
        'attrs',
        'certifi',
        'charset-normalizer',
        'colorama',
        'h11',
        'idna',
        'iniconfig',
        'kitano',
        'outcome',
        'packaging',
        'pluggy',
        'Pygments',
        'PySocks',
        'pytest',
        'python-dotenv',
        'requests',
        'selenium',
        'setuptools',
        'sniffio',
        'sortedcontainers',
        'trio',
        'trio-websocket',
        'typing_extensions',
        'urllib3',
        'webdriver-manager',
        'websocket-client',
        'wsproto'
    ],
)
