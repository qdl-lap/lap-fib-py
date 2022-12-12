from setuptools import find_packages, setup


with open("README.md", "r") as fh:
    long_description_txt = fh.read()
setup(
    name="lap_fib_py",
    version="0.0.1",
    author="Phu La",
    author_email="la_phu@yahoo.com",
    description="Calculates a Fibonacci number",
    long_description=long_description_txt,
    long_description_content_type="text/markdown",
    url="https://github.com/qdl-lap/lap-fib-py",
    install_requires=[],
    packages=find_packages(exclude=("tests",)),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
    tests_require=['pytest'],
)