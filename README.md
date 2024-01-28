<p align="center">
    <img src="https://github.com/jpjacobpadilla/Google-Colab-Selenium/blob/ecce30fd1f5f151e0c1d946259cf19de33aa8e9d/logo.png?raw=true">
</p>

<p align="center">
    <strong>The best way to use Selenium in Google Colab Notebooks!</strong>
</p>

- Simple setup of Selenium and ChromeDriver.
- Seamless integration with Google Colab.
- Supports Undetected ChromeDriver for more advanced use cases.
<br>

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1MX3xY23Go1STe7LbDMvwf2KaqHpbrVhC?usp=sharing)

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
import google_colab_selenium as gs

driver = gs.Chrome()
# Your code to interact with the driver here
# ...
driver.quit()
```

## Undetected ChromeDriver

```python
import google_colab_selenium as gs

driver = gs.UndetectedChrome()
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
import google_colab_selenium as gs

custom_options = Options()
# Add your custom options here

driver = gs.Chrome(options=custom_options)
```

## Contributing
Contributions are welcome! If you have a suggestion or an issue, please use the issue tracker to let me know.

<br>
<br>

<div align="center">
<h3>Test it out for yourself!</h3>

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1MX3xY23Go1STe7LbDMvwf2KaqHpbrVhC?usp=sharing)
</div>
