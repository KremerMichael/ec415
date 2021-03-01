% speccos.m plot the spectrum of a cosine wave
% ORIGINAL
f=10; phi=0;                % specify frequency and phase
time=2;                     % length of time
Ts=1/100;                   % time interval between samples
t=Ts:Ts:time;               % create a time vector
x=cos(2*pi*f*t+phi);        % create cos wave
plotspec(x,Ts)              % draw waveform and spectrum

% 3.6 PART A
f = [1, 2, 20, 30]; phi = 0;
time = 2;
Ts = 1/100;
t = Ts:Ts:time;
for i=1:length(f)
    x=cos(2*pi*f(i)*t+phi);
    plotspec(x, Ts)
end

% 3.6 PART B
f = 10; phi = [0, 0.1, pi/8, pi/2];
time = 2;
Ts = 1/100;
t = Ts:Ts:time;
for i=1:length(phi)
    x=cos(2*pi*f*t+phi(i));
    plotspec(x, Ts)
end

% 3.6 PART C
f = 10; phi = 0;
time = 2;
Ts = [1/10, 1/1000, 1/00000];
for i=1:length(Ts)
    t = Ts(i):Ts(i):time;
    x = cos(2*pi*f*t+phi);
    plotspec(x, Ts)
end