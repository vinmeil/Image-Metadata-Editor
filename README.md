# FIT1055 Prototype - Monash University Malaysia

This repository contains two Python scripts, `write_metadata.py` and `read_metadata.py`, developed as a prototype for the unit FIT1055 at Monash University Malaysia.

## Project Description

The `write_metadata.py` script is used to write custom XMP metadata onto images. It takes an image file and a set of metadata as input, and writes the metadata onto the image file.

The `read_metadata.py` script is used to read specific XMP field metadata from images. It takes an image file as input and returns the specified metadata fields.

These scripts serve as a simple demonstration of the prototype my group has decided on for Assignment 2b in FIT1055.

## Installation

To run these scripts, you will need Python installed on your machine. Follow these steps:

1. Clone this repository to your local machine.
2. Navigate to the directory containing the scripts.
3. Run the scripts using Python.

```bash
git clone https://github.com/vinmeil/Image-Metadata-Editor.git
cd <repository-directory>
python write_metadata.py
python read_metadata.py
```

## Usage
`write_metadata.py`

1. Inside the main function, set the name of the custom field for the metadata by replacing the value of the `field` variable with your custom field name.</br>
2. After that, set the value of the custom metadata field you have previously named by replacing the value of the `value` variable with your custom value.</br>

`read_metadata.py`
1. Inside the main function, specify which field you want to read the value of by replacing the value of the `field` variable with the metadata field name you want to read.
2. Decide what to do with the value by declaring your own functions or implementation.

## Contributing
This is a project for a university unit, and is not currently accepting contributions.

## License
This project is licensed under the terms of the MIT license.