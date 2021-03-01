%p3_3b.m
time = 10; % run fo 10 sec
Ts = 1/1000; % ms timescale
t = Ts:Ts:time; % time vector
x = 5*exp(-t); % signal
plotspec(x, Ts) % plot spectrum