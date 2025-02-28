from setuptools import setup, find_packages

with open("README.md") as f:
    long_description = f.read()

setup(
    name="django-pg-copy",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Tim Allen",
    author_email="tallen@wharton.upenn.edu",
    url="https://github.com/FlipperPA/django-pg-copy",
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    setup_requires=["setuptools_scm"],
    use_scm_version=True,
    install_requires=["django-click"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Framework :: Django",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)
