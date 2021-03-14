% Create Noise signal
time=1;                     % length of time
Ts=1/10000;                 % time interval between samples
t=Ts:Ts:time;               % create time vector
x=randn(1,time/Ts);         % Ts points of noise for time seconds
h=exp(-t);                  % define impulse response
y=conv(h,x);                % Do convolution
subplot(3,1,1), plot(t,x)   % Plot
subplot(3,1,2), plot(t,h)
subplot(3,1,3), plot(t,y(1:length(t)))
% actual commands used to draw figure:
subplot(3,1,1), plot(t,x)
ylabel('input')
subplot(3,1,2), plot(t,h)
ylabel('impulse response')
subplot(3,1,3), plot(t,y(1:length(t)))
ylabel('output')
xlabel('time in seconds')