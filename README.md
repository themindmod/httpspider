#LittleSpider

A little python script that interactively ask for a list of Ip, one per line, ask for a keyword, and than search for that keyword in the http response of the GET request made on port 80 for the given ip. Added the option to convert an ip list made from masscan (via the > redirection, ex "masscan -p 80 0.0.0.0 > test.txt"), and the ability of split the resulted Ips list for bigger works. Output the results in a "givenkeyword"-result.txt file
