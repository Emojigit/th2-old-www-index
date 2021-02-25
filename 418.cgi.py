#!/usr/bin/python3
print("Status: 418 I'm a teapot")
print("Content-Type: text/html")
print()
print(open("/var/www/html/main/418.html").read())
