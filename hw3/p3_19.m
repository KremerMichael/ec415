f1=100; f2=150;                    % specify frequency
time=2;                            % length of time
Ts=1/1000;                         % time interval between samples
t=Ts:Ts:time;                      % create a time vector
x=cos(2*pi*f1*t) + cos(2*pi*f2*t); % create cos wave
y=x.*x;
plotspec(y,Ts)                     % draw waveform and spectrum