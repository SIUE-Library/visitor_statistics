# visitor_statistics
Script for parsing network traffic logs to derive statistics.


Requires a directory of logs to run.

Syntax is as follows:
python3 log_parser.py [log_directory] [regex file] [output file]

#prints out the start and end points of all data base blocks within range based off coordinates
python3 filter.py <ip database>

#given a close range of ip addresses in a file called 'close' and a medium range of
#ip addresses in a file called 'medium', prints range of all incoming ip addresses
python3 inrange.py <incoming IP addresses file>

TODO:
  Parse logs by the minute (assume multiple requests sent within 1 minute belong to the same access)
    -That will reduce the number of requests to a more manageable amount, more reasonable stats
    
