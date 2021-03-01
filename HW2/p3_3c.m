%p3_3c.m
time = 2; % run fo 10 sec
Ts = 1/1000; % ms timescale
t = (0-time):Ts:time; % time vector from -time to time
x = 5*exp(-t); % signal
plotspec(x, Ts) % plot spectrum