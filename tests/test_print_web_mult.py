import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from metamorproxies.soldier import PrintWeb


def print_web(i):
    url = "https://x.com"
    output_path = f"prints/screenshot_x_{i}.png"
    pw = PrintWeb(url, output_path)
    pw.add_argument("--hide-scrollbars")
    pw.take_screenshot()
    pw.kill_driver()
    assert os.path.exists(output_path)
    #os.remove(output_path)

def test_multiple_prints():
    for i in range(10):
        print_web(i)
