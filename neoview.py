import os
import shutil
import zipfile

class NeoView:
    def __init__(self):
        print("NeoView initialized. Ready to zip and unzip files.")

    def zip_files(self, source_dir, output_filename):
        """
        Compresses files in the specified directory into a zip file.

        Parameters:
        source_dir (str): Path to the directory containing files to zip.
        output_filename (str): The name of the output zip file.
        """
        print(f"Zipping files from {source_dir} into {output_filename}.zip")
        with zipfile.ZipFile(f"{output_filename}.zip", 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(source_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, start=source_dir)
                    zipf.write(file_path, arcname)
                    print(f"Added {file_path} as {arcname}")

    def unzip_file(self, zip_filename, output_dir):
        """
        Extracts a zip file into the specified directory.

        Parameters:
        zip_filename (str): The path to the zip file to extract.
        output_dir (str): The directory where the files will be extracted.
        """
        print(f"Unzipping {zip_filename} into {output_dir}")
        with zipfile.ZipFile(zip_filename, 'r') as zipf:
            zipf.extractall(output_dir)
            print(f"Extracted all files to {output_dir}")

if __name__ == "__main__":
    nv = NeoView()
    nv.zip_files("example_directory", "example_output")
    nv.unzip_file("example_output.zip", "extracted_files")