% filternoise.m filter a noisy signal three ways
time=3;                          % length of time
Ts=1/10000;                      % time interval between samples
x=randn(1,time/Ts);              % generate noise signal
figure(1),plotspec(x,Ts)         % draw spectrum of input

freqs=[0 0.6 0.61 1];
amps=[1 1 0 0];
b=firpm(100,freqs,amps);         % specify the LP filter
ylp=filter(b,1,x);               % do the filtering
figure(2),plotspec(ylp,Ts)       % plot the output spectrum