from core.table_reader import FileReader


class TableViewer:
    """Class for displaying tables."""
    def __init__(self, fr: FileReader):
        self.fr = fr
        self.__sheets = None
        self.__data_frame = None

    def display(self):
        data = self.fr.read()

        if isinstance(data, dict):  # For Excel files with sheets
            print(f"The file {self.fr.file_path.name} contains the following sheets:")

            self.sheets = list(data.keys())
            for i, s in enumerate(self.sheets):
                print(f"{i + 1}: {s}")

            sheets_index = self.__choose_sheet()
            self.__data_frame = data[self.sheets[sheets_index]]
        else:
            self.__data_frame = data

        print(f"\nThe first table rows from the file {self.fr.file_path.name}:")
        print(self.__data_frame.head())

        print("\nColumns description:")
        print(self.__data_frame.dtypes)

        # Filter what to display
        self.__filter()

    def __choose_sheet(self):
        sheets_amount = len(self.sheets)

        while True:
            try:
                sheet_number = int(input(f"Choose a sheet number between 1 and {sheets_amount}: "))

                if 1 <= sheet_number <= sheets_amount:
                    return sheet_number - 1
                print(f"The number must be between 1 and {sheets_amount}.")
            except ValueError:
                print("Error: the entered value must be a number.")

    def __filter(self):
        while True:
            try:
                column = input("\nEnter a column name to filter, or press Enter to skip: ")

                if column:
                    value = input(f"Enter a value to filter in '{column}', or press Enter to show all values: ")

                    if value:
                        filtered = self.__data_frame[self.__data_frame[column].astype(str).str.contains(value, case=False)]
                    else:
                        filtered = self.__data_frame[column]

                    print(f"\nFilter results:")
                    print(filtered.head())
                else:
                    break
            except KeyError:
                    print(f"Error: the column '{column}' does not exist in the data.")
            except UnicodeDecodeError:
                    print("Error: use only latin letters, numbers and underscores.")
