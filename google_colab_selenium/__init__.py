from google_colab_selenium.exceptions import (
    GoogleColabSeleniumError,
    InstallChromeError,
    ChromeDriverPathError,
    StartingChromeDriverError
)

__all__ = (
    'ChromeDriver', 
    'UndetectedChromeDriver', 
    'Chrome', 
    'UndetectedChrome',
    'GoogleColabSeleniumError',
    'InstallChromeError',
    'ChromeDriverPathError',
    'StartingChromeDriverError'
)


import os
assert 'COLAB_GPU' in os.environ, "This package should only be used in Google Colab Notebooks."


def __getattr__(name):
    if name == 'ChromeDriver' or name == 'Chrome':
        from google_colab_selenium.chromedriver import ChromeDriver
        return ChromeDriver

    if name == 'UndetectedChromeDriver' or name == 'UndetectedChrome':
        from google_colab_selenium.undetected_chromedriver import UndetectedChromeDriver
        return UndetectedChromeDriver

    raise AttributeError(f"module 'google_colab_selenium' has no attribute '{name}'")
