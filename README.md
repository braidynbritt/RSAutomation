# RSAutomation

## Instructions
1. Download the folder named RSAutomation
2. Download the file named install_helper.bat
3. Put both of these at the filepath C:/
4. Right click Windows logo next to search bar
5. Click Termin(Admin)
6. If not in C:/, enter 'cd ..' until you are in C:/
7. Enter in terminal 'start .\install_helper.bat'
8. Wait for installs to finish

## What the files do
### install_helper.bat
This file installs necessary libraries and software so you don't need to deal with it
### get_click.py
This find's where your cursor is on screen. When starting this script, make sure mouse is on the correct display
### auto_click.py
This is the actual automation script that is a Work In Progress

## How to run the .py files
  To run .py files you will need to enter in the terminal 'python3 [filename]'. The auto_click takes arguments that I will further explain later in this.
  To edit the files, you can either use an IDE, notepad++ (I installed for you), or Vim. Depending on the editor, you will type [editor] [filename]. For example, if using notepad++, notepad++ auto_click.py.

## Arguments for auto_click.py (All required to be in correct area of the game)
### smith
      1. bars - You would enter 'python3 auto_click.py smith bars'. This will start smithing rune bars
      2. darts - You would enter 'python3 auto_click.py smith darts'. This will start smithing rune dart tips
### mine
      1. rune - You would enter 'python3 auto_click.py mine rune'. This will start mining rune ore
      2. luminite - You would enter 'python3 auto_click.py mine luminite'. This will start mining luminite
### test
      This argument is for testing purposes only. This is so we can test each function at a time.
