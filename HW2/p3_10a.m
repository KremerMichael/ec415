% filternoise.m filter a noisy signal three ways
time=3;                          % length of time
Ts=1/20000;                      % time interval between samples
x=randn(1,time/Ts);              % generate noise signal
figure(1),plotspec(x,Ts)         % draw spectrum of input

freqs=[0 .05 0.051 1];
amps=[0 0 1 1];
b=firpm(100,freqs,amps);         % specify the HP filter
yhp=filter(b,1,x);               % do the filtering
figure(2),plotspec(yhp,Ts)       % plot the output spectrum