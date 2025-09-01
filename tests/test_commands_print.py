import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from metamorproxies.soldier import PrintWeb


def test_screenshot_commands():
    # Test taking a screenshot
    pw = PrintWeb("https://www.example.com", "example_screenshot.png")
    pw.add_argument("--hide-scrollbars")
    pw.add_argument("--disable-infobars")
    pw.take_screenshot()
    pw.kill_driver()