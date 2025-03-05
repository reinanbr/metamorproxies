import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from metamorproxies.soldier import PrintWeb


def test_print_web():
    url = "https://www.google.com"
    output_path = "screenshot.png"
    PrintWeb(url, output_path).take_screenshot()
    assert os.path.exists(output_path)
    os.remove(output_path)