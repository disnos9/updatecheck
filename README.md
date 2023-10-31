# Update Check
Update Check is currently only available in python.
## How To Configure
### 1. Download checker.py
You will need [Python](https://python.org) to use this program. <b>Anyone who uses this program must also have Python installed, or use a program that can run Python.</b><br><br>
[Download checker.py](https://github.com/disnos9/updatecheck/releases/download/checker/checker.py)<br><br>

### 2. Create your Version file
Go into your own GitHub repository, and add a file named `version.txt`. Add only the version of your program!<Br>
ALLOWED ```1.0```<br>
NOT ALLOWED ```version 1.0 beta```

### 3. Add your version
Put your most recent version into the .txt file. Then, go to the file and copy the <b>RAW</b> code link.

### 4. Put your link into checker.py
Find line 20. It should be `github_file_url = "https://raw.githubusercontent.com/disnos9/updatecheck/main/version.txt"`. Replace the URL with your link. <b>If it does not start with raw.githubusercontent.com, then you need to get the [RAW CODE.](https://docs.github.com/en/enterprise-cloud@latest/repositories/working-with-files/using-files/viewing-a-file)</b>

### 5. Change the `local_version` variable
Change the `local_version` variable to the most recent update of your program. (Line 26)

### 6. Change the "Update" link
This will make it so that the link, when clicked, will go to your website to install the latest version of your program. On Line 35.
