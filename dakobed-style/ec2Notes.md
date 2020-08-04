## EC2 Notes


finally I have found how to log the intital user data scripts

logs seems to be saved at /var/log/
tee reads standard input and writes to standard output and one or more files..


## Bash 

#!/bin/bash -ex
exec > >(tee /var/log/user-data.log|logger -t user-data -s 2>/dev/console) 2>&1
echo BEGIN
date '+%Y-%m-%d %H:%M:%S'
echo END
