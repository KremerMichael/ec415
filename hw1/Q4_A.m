% Carrier Signal at 10 Hz

f_c = 10; % [Hz] - Carrier frequency
time = 3; % [s] - Signal length
Ts = 1/1000; % [s] - Sampling interval ie. time interval between samples
interval_count = time/Ts; % num of intervals
A = ones(1, interval_count); %set array for amplitude
A(1:interval_count/3) = 2; %first third = 2
A(interval_count*2/3:interval_count) = 2; %sthird third = 2
t = Ts:Ts:time;
x = A .* sin(2*pi*f_c*t); %scale by amplitude

figure(1)
plot(t,x); % plot carrier signal
xlabel('Seconds');
ylabel('Amplitude');
title('10 Hz Carrier Signal');