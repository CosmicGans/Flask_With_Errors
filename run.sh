pkill -f myapp
test -f ~/flask/nohup.out && rm ~/flask/nohup.out
nohup python3 ~/flask/myapp.py &> ~/flask/nohup.out