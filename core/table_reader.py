import pandas as pd
import pyreadstat as prs


class FileReader:
    """Abstract class for reading files."""
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        pass


class Sas7bdatFileReader(FileReader):
    """Class for reading SAS7BDAT files."""
    def read(self):
        return prs.read_sas7bdat(self.file_path)[0]


class XportFileReader(FileReader):
    """Class for reading XPORT files."""
    def read(self):
        return prs.read_xport(self.file_path)[0]


class CsvFileReader(FileReader):
    """Class for reading CSV files."""
    def read(self):
        return pd.read_csv(self.file_path, sep="$")


class XlsxFileReader(FileReader):
    """Class for reading XLSX files."""
    def read(self):
        return pd.read_excel(self.file_path, sheet_name=None)
