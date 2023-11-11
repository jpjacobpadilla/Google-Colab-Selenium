class GoogleColabSeleniumError(Exception):
    """Base Google Colab Selenium Exception"""

    report_msg = """\n\t
        If you believe this isn't due to a configuration error on your end, please
        report the issue with any details you can provide about the steps leading
        up to this error.\n

        You can submit your report here:
        https://github.com/jpjacobpadilla/Google-Colab-Selenium/issues/new

        We apologize for any inconvenience!
    """

    default_message = "An error occurred while attempting to initialize/setup Selenium."

    def __init__(self, message = None):
        super().__init__(
            f'{message or self.default_message}{self.report_msg}'
        )


class InstallChromeError(GoogleColabSeleniumError):
    """Exception raised when installation of Chrome fails."""
    pass

class ChromeDriverPathError(GoogleColabSeleniumError):
    """Exception raised when ChromeDriver path cannot be found or is incorrect."""
    pass

class StartingChromeDriverError(GoogleColabSeleniumError):
    """Exception raised when ChromeDriver fails to start."""
    pass