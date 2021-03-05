%p3_3d.m
time = 20; % run fo 20 sec
Ts = 1/1000; % ms timescale
t = (0-time):Ts:time; % time vector from -time to time
x = 5*exp((-t).^2); % signal
plotspec(x, Ts) % plot spectrum