#!/bin/bash
python "C:\Users\advai\Desktop\DaSH Lab 2nd Attempt\Development Question Level 2\server.py"&
start powershell -NoExit -Command "python 'C:\Users\advai\Desktop\DaSH Lab 2nd Attempt\Development Question Level 2\client0.py'" &
start powershell -NoExit -Command "python 'C:\Users\advai\Desktop\DaSH Lab 2nd Attempt\Development Question Level 2\client1.py'" &
start powershell -NoExit -Command "python 'C:\Users\advai\Desktop\DaSH Lab 2nd Attempt\Development Question Level 2\client2.py'"