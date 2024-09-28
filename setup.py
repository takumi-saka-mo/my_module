import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="my_finance_package",  # パッケージの名前を変更
    version="0.0.1",
    author="Takumi Sakamoto",
    author_email="takumi.saka.mo0107@gmail.com",
    license='MIT',
    description="A package to calculate beta values using finance data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/takumi-saka-mo/my_module",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['my_finance'],  # 必要なパッケージを明示的に指定
    python_requires=">=3.7",
    install_requires=[
        "pandas",
        "numpy",
        "scikit-learn",
        "yfinance"
    ],
)