Ts=1/100; time=10;             % sampling interval and total time
t=0:Ts:time;                   % create time vector
h=sinc(10 * (t - time/2));     % define impulse response
plotspec(h,Ts)                 % find and plot frequency response