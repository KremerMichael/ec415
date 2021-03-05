%p3_3e.m
time = 10; % run fo 10 sec
Ts = 1/10000; % ms timescale
t = 0:Ts:time; % time vector
f = 20; phi = 0; % set f and phi
x = sin((2*pi*f*t) + phi); % signal
plotspec(x, Ts) % plot spectrum