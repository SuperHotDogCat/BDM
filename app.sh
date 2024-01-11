source arduino/bin/activate
python3 -m http.server 10000 & declare -i server_pid=$!
python3 app.py -sp $server_pid