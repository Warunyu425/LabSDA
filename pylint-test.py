# pylint_test.py

"""
Module documentation for pylint_test.
"""

import os
import subprocess

def run_pylint():
    """
    Run Pylint on all Python files in the current directory.
    """
    python_files = [file for file in os.listdir() if file.endswith('.py')]

    if not python_files:
        print("No Python files found.")
        return

    for python_file in python_files:
        file_path = os.path.join(os.getcwd(), python_file)
        subprocess.run(['pylint', file_path], check=True)

if __name__ == "__main__":
    run_pylint()
