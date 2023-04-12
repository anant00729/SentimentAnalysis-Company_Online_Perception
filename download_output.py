import requests
import zipfile
import gdown
import shutil


def download_output() -> None:
    """
    This function downloads output.zip from google drive
    :return: None
    """
    # CITATION: https://drive.google.com/file/d/1C4sxd3439a6lAoK5X3K-CfE1WmhcjsH2/view?usp=share_link
    url = 'https://drive.google.com/uc?id=1C4sxd3439a6lAoK5X3K-CfE1WmhcjsH2'
    output = 'output.zip'
    gdown.download(url, output, quiet=False)
    "https://drive.google.com/file/d/1C4sxd3439a6lAoK5X3K-CfE1WmhcjsH2/view?usp=sharing"


def unzip_and_rollout_output() -> None:
    """
    This function unzips and rolls out the output to the appropriate location
    :return:  None
    """
    with zipfile.ZipFile("output.zip", 'r') as zip_ref:
        for file_name in zip_ref.namelist():
            file_path = zip_ref.extract(file_name)
            shutil.move(file_path, file_path)


def main():
    """
    This function downloads output.zip, the zip file containing all outputs in this project and roll the output out to appropriate place
    :return: 
    """
    download_output()

    unzip_and_rollout_output()


if __name__ == "__main__":
    main()
