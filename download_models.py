import gdown
import shutil
import os


def download_and_move_model(gdrive_id: str, name:str, destination: str) -> None:
    """
    This function downloads a file from google drive and moves it to the destination
    :param gdrive_id: Google drive id of the file
    :param name: Name of the file
    :param destination: Distination path of the file
    :return:
    """
    # Download the file
    # CITATION: https://drive.google.com/file/d/1C4sxd3439a6lAoK5X3K-CfE1WmhcjsH2/view?usp=share_link
    url = f"https://drive.google.com/uc?id={gdrive_id}"
    gdown.download(url, name, quiet=False)

    if not os.path.exists(destination):
        os.makedirs(destination)

    # Moves the file to the destination
    shutil.move(name, f"{destination}/{name}")


def main():
    # Downloading Bert
    download_and_move_model(gdrive_id="1k2CgP6LlB5AeaNbRgJarDQ3aCNtfao0U", name="bert-base-uncased_4000_0.pt", destination="bert/checkpoints")
    download_and_move_model(gdrive_id="1lOH26UZ_yN-A2cdaBt0YJoguOVXvw1TL", name="lstm-base-uncased_4000_0_best.h5", destination="lstm/checkpoints")


if __name__ == "__main__":
    main()
