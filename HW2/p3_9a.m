% filternoise.m filter a noisy signal three ways
time=3;                          % length of time
Ts=1/10000;                      % time interval between samples
x=randn(1,time/Ts);              % generate noise signal
figure(1),plotspec(x,Ts)         % draw spectrum of input

freqs=[0 0.74 0.76 1];
amps=[0 0 1 1];
b=firpm(100,freqs,amps);         % specify the HP filter
yhp=filter(b,1,x);               % do the filtering
figure(4),plotspec(yhp,Ts)       % plot the output spectrum