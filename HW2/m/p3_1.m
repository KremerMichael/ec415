% specsquare.m plot the spectrum of a square wave
f = 10;                   % "frequency" of square wave, 10
time = 2;                % length of time, 2
Ts = 1/10000;             % time interval between samples, 1/1000
t = Ts:Ts:time;          % create a time vector
x = sign(cos(2*pi*f*t)); % square wave = sign of cos wave
plotspec(x,Ts)           % call plotspec to draw spectrum