README

Going to abbreviate this:
Command Palette = CTRL+SHIFT+P = CSP

To commit changes or create a repository thing.
1. Log into Github first, create your repo, get the https:// url for the repo
2. In sublime, get used to the CTRL+SHIFT+P for the command pallete
3. CSP do GIT INIT (first time only), hit ENTER a bunch of times
4. If it ask for the name, use master or origin I dunno, haven't read up on git etiquette yet.
5. Enter in the github URL for your repo, that you created earlier in step 1
6. For the project, any and all files, do GIT ADD, then select files (or scroll down and add all) - adds file to 'staging'
		Use Quick ADD.. I don't see any other ADD
7. CSP, GIT COMMIT - add a commit message up top, close window to save. This adds file from 'staging' to 'commit stage...?'
8. CSP, GIT PUSH - push changes to github repo. That's it. 

I don't know about branches and version control, but probably have to read up on that once I start touching other people's code on the company's gitlab :| #pray4meP

This is cool and all, but now I need to figure out how to run python in sublime, so I don't have to open up the IDLE shell. Got it to work. Use SublimeREPL

1. CSP, install package control
2. CSP, package control, install sublimerepl
3. (optional) View > Layout > Rows:2. So you can put python console on the bottome row by dragging the tab to it
4. You get the tab by CSP, launch "SublimeREPL:Python"
5. To run your current code, hold CTRL+, then release both, then press F

SublimeREPL
1. Annoying thing to remember - if you close Sublime, and open it again, need to re-open sublimeREPL for python
2. Tools - SublimeREPL - Python - 'Python - IPython'
3. Then you can start running code in Sublime
4. Shortcut is "CTRL" + "," <- comma. Let go of both, the press "f"