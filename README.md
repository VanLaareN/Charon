# Charon


to generate certificates:

openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes


Problems that were solved:
    - When a file has been modified and sent over, the watchdog will keep on putting the event in the queue which causes the
      Client to keep resending the same file over and over again.
      => Solved by adding the modified files with unique id (path+timedate) to set. It checks if the modification is already in the set, if not it will put it in the queue.
      Unique id needed because otherwise it will just send that file once and it will forever stay in that set and wont be able to be updated again.
