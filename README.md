# Host-Header-Injection-Testing
A tool to check Host Header Injection Vulnerability in websites

## Instructions for direct execution without python or any other dependency installed.
1. Download or Clone the repository.
2. Open the "exeFile" folder.
3. Enter the list of URLs in a text file format specified below.
4. Execute the "program.exe"

![Image of cmdexe](https://raw.githubusercontent.com/Lakshkhandelwal/Host-Header-Injection-Testing/master/TestRun/Images/programexe.png)

5. It will automatically create an ouptut.csv file containing the output.

Caution : Do not rename the input file or exe file.

## Instructions for executing the program.
1. Download or Clone the repository.
2. The program is dependent on the [pycurl](https://pypi.org/project/pycurl/) and [certifi](https://pypi.org/project/certifi/) library so install that using pip .
3. Create an input file in the format specified below.
4. Execute the program from cmd.

  `Command - python program.py`
  
  ![Image of cmd](https://raw.githubusercontent.com/Lakshkhandelwal/Host-Header-Injection-Testing/master/TestRun/Images/programcmd.png)

5. It will automatically create an output.csv file containing the output.

 ![Image of output](https://raw.githubusercontent.com/Lakshkhandelwal/Host-Header-Injection-Testing/master/TestRun/Images/output.png)

## Input Format
The input format that program accepts is a text file containing list of urls at each line, the image below shows the input format.

![Image of input](https://raw.githubusercontent.com/Lakshkhandelwal/Host-Header-Injection-Testing/master/TestRun/Images/input.png)


## LICENSE
This repository is licensed under the MIT License - see the LICENSE file for details.
