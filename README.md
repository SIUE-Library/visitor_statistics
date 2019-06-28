# visitor_statistics
Script for parsing network traffic logs to derive statistics.


Requires a directory of logs to run.

Syntax is as follows:
python3 log_parser.py [log_directory] [regex file] [output file]

#prints out the start and end points of all data base blocks within range based off coordinates
<br>python3 filter.py [ip database]

#given a close range of ip addresses in a file called 'close' and a medium range of
#ip addresses in a file called 'medium', prints range of all incoming ip addresses
<br>python3 inrange.py [incoming IP addresses file]

sortedDist contains a list of all IP addresses sorted in integer format with informatin regarding country, city, etc, as well of if it is far, medium, or close

TODO:
  Parse logs by the minute (assume multiple requests sent within 1 minute belong to the same access)
    -That will reduce the number of requests to a more manageable amount, more reasonable stats

  <br>
  Change how inrange.py works
    -for each ip address from the log, convert it to int and binary search the sortedDist list for the largest starting address that is smaller than that ip.
    -If the ending address for that block is larger that this ip address then this visitor is from that block
    -Using the other information on that line print out the location and distance category
    -Estimated complexit nlgn (down from nk)
    
