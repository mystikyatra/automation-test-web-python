# Commit and Push
git init
git add README.md
git commit -m "first commit"
git branch -M master
git remote add origin https://github.com/mystikyatra/automation-test-web-python.git
git push -u origin master

# Activate venv
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
.\venv\Scripts\Activate

# Clear pycache
Remove-Item -Recurse -Force .\pages\__pycache__\

# Open powershell run the below shell script to Start Jenkins and automation Video recorder
PS D:\automation-tst-projects\automation-test-web-python> powershell.exe -ExecutionPolicy Bypass -File .\Start-Jenkins-WithScreenRecording.ps1

# Run automation tests
    1. Whole test programs: python -m pytest
    2. Run specific test file only: python -m pytest .\tests\common_test.py
    3. Run specific funtion only: 

# Install requirements.txt
pip install -r .\requirements.txt

# Build periodically in Jenkins (0 13 * * *)
    - 0 → minute 0
    - 13 → hour 13 (PM)
    - * → every day
    - * → every month
    - * → every day of the week