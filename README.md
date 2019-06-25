# visitor_statistics
Script for parsing network traffic logs to derive statistics.


Requires a directory of logs to run.

Syntax is as follows:
python3 log_parser.py [log_directory] [regex file] [output file]


TODO:
  Parse logs by the minute (assume multiple requests sent within 1 minute belong to the same access)
    -That will reduce the number of requests to a more manageable amount, more reasonable stats
    
