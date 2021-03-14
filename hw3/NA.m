% speccos.m plot the spectrum of a cosine wave
f1=40; f2=20;                % specify frequency and phase
time=2;                     % length of time
Ts=1/1000;                   % time interval between samples
t=Ts:Ts:time;               % create a time vector
x=cos(pi*f1*t) + sin(pi*f2*t);        % create cos wave
plotspec(x,Ts)              % draw waveform and spectrum