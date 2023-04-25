from setuptools import setup

with open('requirements.txt') as f:
    install_requirements = f.read().splitlines()

if __name__ == "__main__":
    setup(requires=install_requirements)
