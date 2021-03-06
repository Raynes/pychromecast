"""
Errors to be used by PyChromecast.
"""


class PyChromecastError(Exception):
    """ Base error for PyChromecast. """
    pass


class NoChromecastFoundError(PyChromecastError):
    """
    When a command has to auto-discover a Chromecast and cannot find one.
    """
    pass


class MultipleChromecastsFoundError(PyChromecastError):
    """
    When getting a singular chromecast results in getting multiple chromecasts.
    """
    pass


class ChromecastConnectionError(PyChromecastError):
    """ When a connection error occurs within PyChromecast. """
    pass


class NotConnected(PyChromecastError):
    """
    Raised when a command is invoked while not connected to a Chromecast.
    """
    pass


class UnsupportedNamespace(PyChromecastError):
    """
    Raised when trying to send a message with a namespace that is not
    supported by the current running app.
    """
    pass
