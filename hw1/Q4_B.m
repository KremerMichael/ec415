time = 3; % [s] - Signal length
Ts = 1/1000; % [s] - Sampling interval ie. time interval between samples
interval_count = time/Ts; % num of intervals

fc = 10; % 10 Hz carrier freq
f_c_arr = ones(1, interval_count); % [Hz] - Carrier frequency array
df = 5; % [Hz]

%changing freq in array
f_c_arr(1:interval_count/3) = fc + df;
f_c_arr(interval_count/3:interval_count*2/3) = fc - df;
f_c_arr(interval_count*2/3:interval_count) = fc + df;


t = Ts:Ts:time;
x = sin(2*pi*(f_c_arr.*t));

figure(1)
plot(t,x); % plot carrier signal
xlabel('Seconds');
ylabel('Amplitude');
title('10 Hz Carrier Signal');