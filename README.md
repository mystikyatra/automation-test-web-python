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
Remove-Item -Recurse -Force .\__pycache__\

