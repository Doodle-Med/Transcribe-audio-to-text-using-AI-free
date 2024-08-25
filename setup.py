from setuptools import setup, find_packages

setup(
    name="transcriptiontool",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pydub",
        "SpeechRecognition",
    ],
    entry_points={
        "console_scripts": [
            "transcribe=transcriptiontool.Transcribe:main",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple tool to transcribe audio files to text using Python.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jhennig3/Transcribe-audio-to-text-using-AI-free",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
