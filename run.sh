pkill -f myapp
test -f ~/flask/nohup.out && rm ~/flask/nohup.out
nohup python3 myapp.py &> ~/flask/nohup.out