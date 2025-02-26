# First thing to do (only once)
git clone https://github.com/Archer-SN/Mani-Kukuraya.git

# To save code
git add .

git commit -m "Message here"

git push origin master

# To update code from friends
git pull origin master

# Run program with
uvicorn main:app --reload-dir
