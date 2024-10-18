import unittest
import os
import subprocess

class TestMainScript(unittest.TestCase):
    def test_plot_generation(self):

        result = subprocess.run(['python3', 'main.py'], capture_output=True, text=True)
        
        self.assertEqual(result.returncode, 0, msg="main.py did not run successfully")
        
        self.assertTrue(os.path.exists("plot.png"), msg="plot.png was not created")

        if os.path.exists("plot.png"):
            os.remove("plot.png")

if __name__ == '__main__':
    unittest.main()