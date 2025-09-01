import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from metamorproxies.soldier import PrintWeb



def test_setup_driver():
    pw = PrintWeb("https://www.example.com", "example_screenshot.png")
    driver = pw.setup_driver()
    assert driver is not None
    driver.quit()