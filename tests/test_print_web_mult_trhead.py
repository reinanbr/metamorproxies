import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from metamorproxies.soldier import PrintWeb
import threading

Thread = threading.Thread

def print_web(i):
    url = "https://x.com"
    output_path = f"prints/screenshot_x_thread_{i}.png"
    pw = PrintWeb(url, output_path)
    pw.add_argument("--hide-scrollbars")
    pw.take_screenshot()
    pw.kill_driver()
    assert os.path.exists(output_path)
    #os.remove(output_path)

def test_multiple_thread():
    threads = []
    for i in range(10):
        thread = Thread(target=print_web, args=(i,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()