import os
import zipfile


def traverse_path(path: str) -> list:
    """
    Recursively traverses the given path and extracts the results in the path
    :param path: Path to traverse
    :return: List of files found
    """
    paths = []
    for root, dirs, files in os.walk(path):
        if ("/data" in root) | ("/results" in root):
            for file in files:
                file_path = os.path.join(root, file)
                paths.append(file_path)

    return paths


def main():
    """
    This script traverses each directory and zips up the data and results.  The results are then manually uploaded to google drive
    :return: None
    """
    files_to_zip = []
    for directory in ["./bert", "./nyt", "./result_visualizations", "training_data_formulation", "./twitter", "./lstm"]:
        files_to_zip += traverse_path(directory)

    files_to_zip.append("./README.md")

    num_files_to_zip = len(files_to_zip)
    with zipfile.ZipFile("output.zip", 'w', compression=zipfile.ZIP_DEFLATED) as zip_file:
        for count, file in enumerate(files_to_zip):
            print(f"{round(100 * count / num_files_to_zip)}% Complete")
            zip_file.write(file, os.path.relpath(file, "./"))


if __name__ == "__main__":
    main()
