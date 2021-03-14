f1=100; f2=125;                    % specify frequency
time=2;                            % length of time
Ts=1/100;                          % time interval between samples
t=Ts:Ts:time;                      % create a time vector
x=cos(2*pi*f1*t) + cos(2*pi*f2*t); % create cos wave
y = abs(x);                        % Take abs value
plotspec(y,Ts)                     % draw waveform and spectrum