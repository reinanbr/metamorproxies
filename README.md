<p align="center">
  <img src="https://raw.githubusercontent.com/reinanbr/logos/refs/heads/main/metamorproxies.jpg?token=GHSAT0AAAAAAC7ZO2HDGG524ZEG4KTRLJWWZ6HTTDQ" alt="MetamorProxies Logo" width="450"/>
</p>
<h1 align="center">MetamorProxies</h1>
<p align="center">
  <a href="https://github.com/your-username/metamorproxies/actions">
    <img src="https://img.shields.io/github/workflow/status/your-username/metamorproxies/CI" alt="CI Status">
  </a>
  <a href="https://codecov.io/gh/your-username/metamorproxies">
    <img src="https://img.shields.io/codecov/c/github/your-username/metamorproxies" alt="Code Coverage">
  </a>
  <a href="https://pypi.org/project/metamorproxies/">
    <img src="https://img.shields.io/pypi/v/metamorproxies" alt="PyPI Version">
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License">
  </a>
</p>

---

MetamorProxies is a Python library that provides a collection of tools to manipulate, manage, and use proxies in web scraping, automation, or other network tasks. This library aims to simplify the handling of proxy servers, allowing users to seamlessly rotate, filter, and configure proxies in a clean, efficient manner.

## Features

* **Proxy Rotation** : Easily rotate proxies to avoid being blocked by target servers.
* **Custom Proxy Configuration** : Configure proxies to fit your unique needs.
* **Integration** : Designed to integrate with common libraries like `requests` for seamless proxy management.
* **Flexible API** : Simple, intuitive API for proxy manipulation and usage.
* **Extensible** : Easy to extend for your own use cases.

## Installation

### Using pip (recommended)

MetamorProxies is available on PyPI, and you can install it with pip:

```bash
pip install metamorproxies
```

Alternatively, you can install the latest version directly from the GitHub repository:

```bash
pip install git+https://github.com/your-username/metamorproxies.git
```

### From source

Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/metamorproxies.git
cd metamorproxies
pip install -r requirements.txt
python setup.py install
```

## Usage

Here’s a simple example of how to use MetamorProxies with `requests` to rotate proxies.

```python
import requests
from metamorproxies import ProxyManager

# Initialize ProxyManager
proxy_manager = ProxyManager()

# Get a random proxy from your list
proxy = proxy_manager.get_proxy()

# Use the proxy with requests
response = requests.get("https://example.com", proxies={"http": proxy, "https": proxy})

print(response.text)
```

### Advanced Usage

#### Configuring Proxies

You can configure your proxy manager with a list of proxies or use different strategies for proxy rotation. Here's an example:

```python
from metamorproxies import ProxyManager

proxy_list = [
    "http://user:pass@proxy1.com:8080",
    "http://user:pass@proxy2.com:8080",
    "http://user:pass@proxy3.com:8080"
]

proxy_manager = ProxyManager(proxies=proxy_list)
```

#### Customizing Proxy Rotation Strategy

MetamorProxies allows you to customize how proxies are rotated or selected, making it suitable for specific use cases, such as avoiding IP bans.

```python
proxy_manager.set_rotation_strategy('round_robin')
```

## Documentation

For more detailed documentation on how to use MetamorProxies and all its features, check out the [documentation](https://your-project-docs.com/).

## Contributing

We welcome contributions from the community! If you’d like to contribute to MetamorProxies, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit them (`git commit -am 'Add feature'`).
4. Push to your branch (`git push origin feature-name`).
5. Open a pull request.

Please make sure your code follows the existing style conventions, and include tests for new features or fixes.
