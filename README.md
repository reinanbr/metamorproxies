<p align="center">
  <img src="/img/metamorproxies.jpg" alt="MetamorProxies Logo" width="450"/>
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

MetamorProxies is a Python library that provides tools for web automation and proxy management. This library includes functionality for taking website screenshots and testing SOCKS5 proxies, making it useful for web scraping, automation, and network testing tasks.

## Features

* **Website Screenshots** : Capture screenshots of websites using headless Chrome browser
* **Proxy Testing** : Test SOCKS5 proxies for functionality and reliability
* **Proxy Management** : Fetch and validate proxy lists from external sources
* **Headless Automation** : Run browser automation without GUI
* **Flexible Configuration** : Customizable screenshot settings and proxy testing parameters

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

### Taking Website Screenshots

The main functionality of MetamorProxies is capturing screenshots of websites using the `PrintWeb` class:

```python
from metamorproxies.soldier import PrintWeb

# Initialize PrintWeb with URL and output path
url = "https://www.example.com"
output_path = "screenshot.png"
printer = PrintWeb(url, output_path)

# Take the screenshot
printer.take_screenshot()
print(f"Screenshot saved as {output_path}")
```

### Advanced Screenshot Usage

You can also change the output path after initialization:

```python
from metamorproxies.soldier import PrintWeb

# Initialize with default output path
printer = PrintWeb("https://www.example.com")

# Change the output path
printer.set_path("custom_screenshot.png")

#Change driver service path
chromedriver_path = os.path.join(os.path.dirname(__file__), '/drivers/', 'chromedriver')
printer.set_service(chromedriver_path)

# Add driver arguments
printer.add_argument("--hide-scrollbars")

# Change the size window
printer.set_window_size(1200,800)

# Take the screenshot
printer.take_screenshot()

# kill the process driver
printer.kill_driver()
```


## Dependencies

MetamorProxies requires the following main dependencies:
- `selenium` - For browser automation
- `webdriver-manager` - For automatic Chrome driver management
- `requests` - For HTTP requests and proxy testing
- `kitano` - Additional utility library

## Documentation

For more detailed documentation on how to use MetamorProxies and all its features, check out the [documentation](https://your-project-docs.com/).

## Contributing

We welcome contributions from the community! If you'd like to contribute to MetamorProxies, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit them (`git commit -am 'Add feature'`).
4. Push to your branch (`git push origin feature-name`).
5. Open a pull request.

Please make sure your code follows the existing style conventions, and include tests for new features or fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
