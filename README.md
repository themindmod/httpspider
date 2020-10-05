HttpSpider

A little python script that interactively ask for a list of Ip, one per line, ask for a keyword, and than search for that keyword in the http response.text of the GET request made on port 80 for the given ip. Added the option to convert an ip list made from masscan (via the > redirection, ex "masscan -p 80 0.0.0.0 > test.txt"), and the ability of split the resulted Ips list for bigger works. Output the results in a "givenkeyword"-result.txt file

Requirements

- python3
- pip  modules = requests, subprocess, colored

Usage

$ > python3 mylittlespider.py
or, make it executable (chmod +x mylittlespider.py) and..
$ > ./mylittlespider

the list containing the Ips must be formatted this way:
http://ip1
http://ip2

Program will autoremove \n, so don't worry about

To import masscan results (Linux only feature), simple point the output of masscan to a file and feed the program with it (es. "masscan -p 80 10.0.0.0/8 > output.txt")

Results are printed in a file at current directory, so make sure to have the right permissions to write.
