f=10; phi=0;                % specify frequency and phase
time=2;                     % length of time
Ts=1/100;                   % time interval between samples
t=Ts:Ts:time;               % create a time vector
x=sign(cos(2*pi*f*t+phi));  % create cos wave
plotspec(x,Ts)              % draw waveform and spectrum