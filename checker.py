'''
      _   _      ___ _    _      _  _     _  _  
 | | |_) | \  /\  | |_   /  |_| |_ /  |/ |_ |_) 
 |_| |   |_/ /--\ | |_   \_ | | |_ \_ |\ |_ | \ 
                     v1.0                              

'''
import requests
import tkinter as tk
import webbrowser

def check_updates():
    print("""
      _   _      ___ _    _      _  _     _  _  
 | | |_) | \  /\  | |_   /  |_| |_ /  |/ |_ |_) 
 |_| |   |_/ /--\ | |_   \_ | | |_ \_ |\ |_ | \ 
          
Checking for updates...
                                                """)
    github_file_url = "https://raw.githubusercontent.com/disnos9/updatecheck/main/version.txt"

    try:
        response = requests.get(github_file_url)
        latest_version = response.text.strip()

        local_version = "1.1"  # Replace this with your current version

        if local_version != latest_version:
            root = tk.Tk()
            root.title("Update Checker")

            message_label = tk.Label(root, text="Your version of this program is out of date. Please download the latest version to continue using this app.")
            message_label.pack()

            redirect_button = tk.Button(root, text="Download Most Recent Version", command=lambda: open_link("https://github.com/disnos9/updatecheck/blob/main/timetoupdate.md"))
            redirect_button.pack()

            root.mainloop()
        else:
           print("User is up to date.")
    except requests.RequestException as e:
        print("Error fetching data:", e)

def open_link(url):
    webbrowser.open_new(url)

check_updates()
