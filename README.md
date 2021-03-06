# pyBeginners
Welcome Python Beginners! Lets get to work

**What you'll need**
- Python
- Git
- Text editor/IDE (I use Sublime 3)
- Patience
- Google/Stack OverFlow/http://learnpythonthehardway.org/book/

**Quick Python installation Guide:**

1) Navigate to https://www.python.org/downloads/

2) Select Python 2.7.10 

3) Choose appropriate version (check what bit architecture your computer supports)

4) Proceed through installer

5) **If not prompted to add Python to the PATH, do the following:**
- Open _Control Panel_
- Click _System_
- Click _Advanced system settings_ (located on the left pane)
- Click _Environment Variables_
- Under _System Variables_, select _Path_
- Click _Edit_
- (Windows 7 Users): Add directory path to python.exe (i.e. C:\Program Files (x86)\python.exe;) to beginning of text entry box REMEMBER TO ADD A SEMICOLON AT THE END OF THE PATH
- (Windows 10 Users): Follow on-screen prompt and add directory path to python.exe

6) Confirm Python is added to PATH:
- Open Command Prompt
- Enter **python**
- If python console initializes, python exists in the PATH (nice going)
- If the console doesn't initialize, double-check that each step has been followed (no big deal, get used to troubleshooting)

  
**Quick Git Guide:**

1) If you haven't already, create a GitHub account (www.github.com)

2) Install Git on your computer (https://git-scm.com/downloads). Proceed with default options **but** select _command window_ and _add to PATH_ options when presented

3) Confirm git is added to PATH:
- Open Command Prompt
- Enter **git**
- If presented with a list of git commands, it has been added (congrats)
- If not presented, attempt to add the GIT to the PATH manually (good luck)

4) Fork the "pyBeginner" repository (https://guides.github.com/activities/forking/)
- Click the **Fork** button located near the top-right side of this page

5) Navigate to http://github.com/"your-username-here"/pyBeginner (this is where your forked repository lives)

6) Work with repository on a local machine:
- Click the clipboard-looking button to retrieve the cloning url (clipboard located to the left of the Download Zip button )
- Open Command prompt in the directory where you'd like to store your exercises (i.e. go to D:\Users\"your name"\Documents\, hold shift + right-click, select "Open command window here")
- Enter the following: **git clone https://github.com/"your-username-here"/pyBeginner.git**  
**This will add all files into that particular directory
- Complete some exercises or start up a project (drag the __.py folder into a text editor)
- Upon completion, within the pyBeginner directory path enter the following in Command Prompt: **git add "edited file-name here"**
- You need to commit the changes with an edit message, enter: **git commit -m "I changed ____ about this file"**
- Enter: **git push**
- Enter proper GitHub credentials upon inquiry (password won't be visbile when typing)
- Confirm that all changes have been pushed by navigating to http://github.com/"your-username-here"/pyBeginner


Those are the basics, now go CODE!
