"""
lfs_help_plugin - A LichtFeld Studio Help & Reference plugin.
Provides keyboard shortcuts reference and other useful information.
"""

import lichtfeld as lf
from .panels.help_panel import HelpPanel

_classes = [HelpPanel]


def on_load():
    """Called when plugin is loaded."""
    for cls in _classes:
        lf.register_class(cls)
    lf.log.info("lfs_help_plugin loaded")


def on_unload():
    """Called when plugin is unloaded."""
    for cls in reversed(_classes):
        lf.unregister_class(cls)
    lf.log.info("lfs_help_plugin unloaded")
