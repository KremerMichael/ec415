% 3.3 PART A
time = 10; % run fo 10 sec
Ts = 1/10000; % ms timescale
t = Ts:Ts:time; % time vector
x = exp(-t); % signal
plotspec(x, Ts) % plot spectrum