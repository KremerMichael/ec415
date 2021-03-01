% specsquare.m plot the spectrum of a square wave
% ORIGINAL
% f = 10; % "frequency" of square wave
% time = 2; % length of time
% Ts = 1/1000; % time interval between samples
% t = Ts:Ts:time; % create a time vector
% x = sign(cos(2*pi*f*t)); % square wave = sign of cos wave
% plotspec(x,Ts) % call plotspec to draw spectrum

% 3.1 PART A 
% f = 20, 40, 100, 300     
% 3.1 PART B
% time = 1, 10, 100
% 3.1 PART C
% Ts = 1/100, 1/10000

% 3.3 PART A
time = 10;
Ts = 1/1000;
t = Ts:Ts:time;
x = 5*exp(-t);
plotspec(x, Ts)

% s(t) = e^-t ???
% 3.3 PART B
% time = 10
% scale s(t) from PART A by 5
% 3.3 PART C
% 3.3 PART D
% 3.3 PART E
