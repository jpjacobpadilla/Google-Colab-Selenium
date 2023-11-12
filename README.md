# Google-Colab-Selenium
[![PyPI downloads](https://img.shields.io/pypi/dm/google-colab-selenium.svg)](https://pypi.org/project/google-colab-selenium/)

The best way to use Selenium in Google Colab Notebooks!

- Simple setup of Selenium and ChromeDriver.
- Seamless integration with Google Colab.
- Support for undetected ChromeDriver for more advanced use cases.
<br>

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1uApofPD-uTbZQ8dVq2IVTGHZOxdJtiel?usp=sharing)

## Installation  

Basic usage:
```bash
%pip install google-colab-selenium
```

Use [undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver) version:
```bash
%pip install google-colab-selenium[undetected]
```


## Basic Usage
```python
from google_colab_selenium import ChromeDriver

driver = ChromeDriver()
# Your code to interact with the driver here
# ...
driver.quit()
```

## Undetected ChromeDriver

```python
from google_colab_selenium import UndetectedChromeDriver

driver = UndetectedChromeDriver()
# Your code to interact with the driver here
# ...
driver.quit()
```

## Default Options

The `google-colab-selenium` package is preconfigured with a set of default options optimized for Google Colab environments. These defaults include:

- `--headless`: Runs Chrome in headless mode (without a GUI).
- `--no-sandbox`: Disables the Chrome sandboxing feature, necessary in the Colab environment.
- `--disable-dev-shm-usage`: Prevents issues with limited shared memory in Docker containers.
- `--lang=en`: Sets the language to English.

You are welcome to extend or override these options based on your needs:

```python
from selenium.webdriver.chrome.options import Options
from google_colab_selenium import ChromeDriver

custom_options = Options()
# Add your custom options here
# custom_options.add_argument("--your-option")

driver = ChromeDriver(options=custom_options)
```


## Contributing
Contributions are welcome! If you have a suggestion or an issue, please use the issue tracker to let us know.

You can also contact me [here](https://jacobpadilla.com/contact).

<br>

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1uApofPD-uTbZQ8dVq2IVTGHZOxdJtiel?usp=sharing)


![logo](https://raw.githubusercontent.com/jpjacobpadilla/Google-Colab-Selenium/main/logo.png)

