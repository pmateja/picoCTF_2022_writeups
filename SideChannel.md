This one can be done in a more automatic way, but we can spend our _time_ on writing the tool for solving or spend it on doing it by hand.

Program runs like this:

```console
[user@host SideChannel]$ ./pin_checker 
Please enter your 8-digit PIN code:
12345678
8
Checking PIN...
Access denied.
```

but we want to run it in batch mode via pipe:

```console
[user@host SideChannel]$ echo 12345678 | ./pin_checker 
Please enter your 8-digit PIN code: 
8
Checking PIN...
Access denied.
```

And one more thing, we want to use the *time* command as well, to see it the execution time will be different on different input:

```console
[user@host SideChannel]$ echo 11111111 | time ./pin_checker 
Please enter your 8-digit PIN code:
8
Checking PIN...
Access denied.
Command exited with non-zero status 1
0.13user 0.00system 0:00.14elapsed 100%CPU (0avgtext+0avgdata 6140maxresident)k
0inputs+0outputs (0major+143minor)pagefaults 0swaps
[user@host SideChannel]$ echo 21111111 | time ./pin_checker 
Please enter your 8-digit PIN code:
8
Checking PIN...
Access denied.
Command exited with non-zero status 1
0.15user 0.00system 0:00.15elapsed 99%CPU (0avgtext+0avgdata 6104maxresident)k
0inputs+0outputs (1major+144minor)pagefaults 0swaps
[user@host SideChannel]$ echo 31111111 | time ./pin_checker 
Please enter your 8-digit PIN code:
8
Checking PIN...
Access denied.
Command exited with non-zero status 1
0.16user 0.00system 0:00.16elapsed 99%CPU (0avgtext+0avgdata 6076maxresident)k
0inputs+0outputs (0major+141minor)pagefaults 0swaps
[user@host SideChannel]$ echo 41111111 | time ./pin_checker 
Please enter your 8-digit PIN code:
8
Checking PIN...
Access denied.
Command exited with non-zero status 1
0.26user 0.00system 0:00.26elapsed 99%CPU (0avgtext+0avgdata 6124maxresident)k
0inputs+0outputs (0major+143minor)pagefaults 0swaps
```

We can see that the user time is higher for the number **4** in the first positon, that shows us, that this part is correct. 7 more digits to go... But as the time is significantly higher, we do not have to test every digit from 0 to 9 every time, just till the time will show us what we want. 

In the end it looks like:

```console
[user@host SideChannel]$ echo 48390513 | time ./pin_checker     
Please enter your 8-digit PIN code:
8
Checking PIN...
Access granted. You may use your PIN to log into the master server.
```

Last step is to get the flag from the server via the correct pin. It takes a bit of patience, but it's really simple
