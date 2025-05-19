from pathlib import Path
from argparse import ArgumentParser
from typing import Optional, Sequence

from core.zip_extractor import ZipUnarchiver
from core.table_viewer import TableViewer
from core.table_reader import Sas7bdatFileReader, XportFileReader, CsvFileReader, XlsxFileReader


def create_file_reader(file_path: Path):
    exten = file_path.suffix.lower()
    if exten == ".sas7bdat":
        return Sas7bdatFileReader(file_path)
    elif exten == ".xpt":
        return XportFileReader(file_path)
    elif exten == ".csv":
        return CsvFileReader(file_path)
    elif exten == ".xlsx":
        return XlsxFileReader(file_path)
    else:
        return None


def main(argv: Optional[Sequence] = None):
    resources_path = Path("resources")
    parser = ArgumentParser(description="Zip files")
    parser.add_argument("source", help="ARCHIVES", type=str, nargs="*")
    args = parser.parse_args(argv)

    if not args.source:
        zip_files = list(resources_path.glob("*.zip"))

        if not zip_files:
            print("No zip files found in resources folder.")
            return

        args.source = [zip_file.name for zip_file in zip_files]

    for archive_name in args.source:
        archive_path = resources_path / archive_name

        try:
            unarchiver = ZipUnarchiver(archive_path)
            unarchiver.extract()
        except Exception as e:
            print(f"Error: {e}")

    data_path = Path(ZipUnarchiver.DATA_DIR)

    for file_path in data_path.rglob("*"):
        if file_path.is_file():
            file_reader = create_file_reader(file_path)
            if file_reader:
                table = TableViewer(file_reader)
                table.display()
                to_continue = input("\nPress Enter to move to the next table, or type 'exit' to exit: ")

                if  to_continue.strip().lower() == "exit":
                    print("Interrupted by user.")
                    break
            else:
                print(f"No file reader found for {file_path}. "
                       "The program only reads files with the following extensions: .sas7bdat, .xpt, .csv, .xlsx")
    else:
        print("All files have been processed.")


if __name__ == "__main__":
    main()
