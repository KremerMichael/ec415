% Carrier Signal at 10 Hz

f_c = 10; % [Hz] - Carrier frequency
time = 3; % [s] - Signal length
Ts = 1/1000; % [s] - Sampling interval ie. time interval between samples
t = Ts:Ts:time;
x = sin(2*pi*f_c*t);

figure(1)
plot(t,x); % plot carrier signal
xlabel('Seconds');
ylabel('Amplitude');
title('10 Hz Carrier Signal');

