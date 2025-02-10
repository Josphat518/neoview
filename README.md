# NeoView

NeoView is a simple Python utility that leverages native Windows capabilities to efficiently zip and unzip files. It provides a command-line interface to manage compressed files with ease.

## Features

- **Zip Files:** Compress files from a specified directory into a single `.zip` file.
- **Unzip Files:** Extract the contents of a `.zip` file into a specified directory.

## Requirements

- Python 3.x
- Windows OS

## Installation

Clone the repository and navigate into the project directory:

```sh
git clone https://github.com/yourusername/neoview.git
cd neoview
```

## Usage

Run `neoview.py` to zip or unzip files:

### Zipping Files

To compress files from a directory:

```python
nv = NeoView()
nv.zip_files("path/to/source_directory", "name_of_output_zip_file")
```

- `path/to/source_directory`: The path to the directory you want to compress.
- `name_of_output_zip_file`: The desired name for the output zip file (without the `.zip` extension).

### Unzipping Files

To extract files from a zip archive:

```python
nv.unzip_file("path/to/zip_file.zip", "path/to/output_directory")
```

- `path/to/zip_file.zip`: The path to the zip file you want to extract.
- `path/to/output_directory`: The directory where the extracted files will be placed.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## Contact

For any questions or feedback, please contact [your-email@example.com](mailto:your-email@example.com).