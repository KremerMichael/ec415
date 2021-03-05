% filternoise.m filter a noisy signal three ways
time=3;                          % length of time
Ts=1/10000;                      % time interval between samples
x=randn(1,time/Ts);              % generate noise signal
figure(1),plotspec(x,Ts)         % draw spectrum of input

freqs=[0 0.15 0.151 0.25 0.251 1];
amps=[0 0 1 1 0 0];
b=firpm(100,freqs,amps);         % BP filter
ybp=filter(b,1,x);               % do the filtering
figure(3),plotspec(ybp,Ts)       % plot the output spectrum