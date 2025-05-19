import os
import zipfile


class ZipUnarchiver:
    """Class for extracting ZIP archives."""
    DATA_DIR = "data"  # folder for extracted files

    def __init__(self, archive_path):
        self.archive_path = archive_path
        os.makedirs(self.DATA_DIR, exist_ok=True)

    def extract(self):
        try:
            with zipfile.ZipFile(self.archive_path, "r") as zf:
                zf.extractall(self.DATA_DIR)
        except zipfile.BadZipFile:
            print(f"Error: {self.archive_path} is not a correct ZIP archive.")

        return os.path.join(self.DATA_DIR)
