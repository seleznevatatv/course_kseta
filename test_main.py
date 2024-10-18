import unittest
import os
import subprocess


class TestMainScript(unittest.TestCase):
    def test_plot_generation(self):
        # Run the main.py script
        result = subprocess.run(["python3", "main.py"], capture_output=True, text=True)

        # Check if the script ran without errors
        self.assertEqual(
            result.returncode,
            0,
            msg=f"main.py did not run successfully. stdout: {result.stdout}, stderr: {result.stderr}",
        )

        # Check if the plot.png file is created
        self.assertTrue(os.path.exists("plot.png"), msg="plot.png was not created")

        # Clean up the generated plot.png file
        if os.path.exists("plot.png"):
            os.remove("plot.png")


if __name__ == "__main__":
    unittest.main()
