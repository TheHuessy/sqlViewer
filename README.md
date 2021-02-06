## Lazy Man's pgAdmin
I just installed pgAdmin on my ubuntu machine only to find that it wouldn't hit my in-house postgres server without crashing. The internet had few helpful resources, I tried installing the admin pack, I ran the program as sudo, etc., etc., nothing was working.

Since I built the postgres server and have been able to hit it from other linux machines and windows machines and since I only wanted to use it to look at data in the database, I'm just going to write a python tool that will allow me to:

* Execute SQL queries from the command line
* View results in the terminal window

This is my Lazy Programmer way of fixing an annoying blocker.

## Things to add:

* Need to add row return limit, current code has issues with large row returns.

