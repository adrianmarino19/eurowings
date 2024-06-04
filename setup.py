from setuptools import find_packages
from setuptools import setup

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(name='takeoff',
      description="Takeoff Models",
      license="MIT",
      author="Le Wagon",
      author_email="adrianmarino@alumni.ie.edu",
      install_requires=requirements,
      packages=find_packages(),
      #test_suite="tests",
      #include_package_data: to install data from MANIFEST.in
      include_package_data=True,
      zip_safe=False)
