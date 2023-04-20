pkill -f myapp
test -f nohup.out && rm nohup.out
nohup python3 myapp.py &