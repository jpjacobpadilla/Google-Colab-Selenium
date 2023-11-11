def __getattr__(name):
    if name == 'ChromeDriver':
        from google_colab_selenium.chromedriver import ChromeDriver
        return getattr(ChromeDriver, name)

    if name == 'UndetectedChromeDriver':
        from google_colab_selenium.undetected_chromedriver import UndetectedChromeDriver
        return getattr(UndetectedChromeDriver, name)

    raise AttributeError(f"module 'my_package' has no attribute '{name}'")
