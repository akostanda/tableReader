# tableReader
This is an example of table reader using Python.

The program reads files with the following extensions: .sas7bdat, .xpt, .csv, .xlsx
and displays the content of the tables in the console.


## Technologies
* Python


# Project settings
1. Clone this project's repository to your local machine using SSH
    ```bash
      git clone git@github.com:akostanda/tableReader.git
    ```
2. Move to it
    ```bash
      cd <your project name>
    ```
3. Install the necessary dependencies:
    ```bash
      pip install -r requirements.txt
    ```
4. Put needed archives with data files in the resources folder.
5. Project run  
   To run the certain archives, use:
    ```bash
      python main.py <archive_name_1> <archive_name_2> ...
    ```
    To run all archives in the resources folder, use:
    ```bash
      python main.py
    ```
6. Follow the instructions in the console


## Addition information
Now for testing purpose, the program works only with .zip files. It is not a problem to add other archive and file types.