Ts=1/100; time=10;             % sampling interval and total time
t=0:Ts:time;                   % create time vector
h=sin(25*t);                   % define impulse response
plotspec(h,Ts)                 % find and plot frequency response