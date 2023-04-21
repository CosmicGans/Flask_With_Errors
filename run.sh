pkill -f myapp
test -f ~/flask/nohup.out && rm ~/flask/nohup.out
nohup python3 ~/flask/myapp.py 2>&1 ~/flask/nohup.out &