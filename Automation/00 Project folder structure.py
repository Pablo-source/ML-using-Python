import os
from os import path


def project_setup():
    if not path.exists("data"):
        os.mkdir("data")
    if not path.exists("model"):
        os.mkdir("model")
    if not path.exists("output"):
        os.mkdir("output")
    if not path.exists("tests"):
        os.mkdir("tests")
    print("Created project folder structure")


project_setup()
