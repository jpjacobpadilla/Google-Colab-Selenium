def __getattr__(name):
    if name == 'ChromeDriver':
        from google_colab_selenium.chromedriver import ChromeDriver
        return ChromeDriver

    if name == 'UndetectedChromeDriver':
        from google_colab_selenium.undetected_chromedriver import UndetectedChromeDriver
        return UndetectedChromeDriver

    raise AttributeError(f"module 'google_colab_selenium' has no attribute '{name}'")
