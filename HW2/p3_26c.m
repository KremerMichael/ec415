% modulate.m: change the frequency of the input
time=.5; Ts=1/10000;          % time and sampling interval
t=Ts:Ts:time;                 % define a 'time' vector
fc=1000; cmod=cos(2*pi*fc*t); % create cos of freq fc
rand_sig=randn(1,time/Ts);    % generate noise signal
freqs=[0 0.06 0.061 1];
amps=[1 1 0 0];
b=firpm(100,freqs,amps);      % specify the LP filter
x=filter(b,1,rand_sig);       % do the filtering
y=cmod.*x;                    % multiply input by cmod
figure(1), plotspec(cmod,Ts)  % find spectra and plot
figure(2), plotspec(x,Ts)
figure(3), plotspec(y,Ts)

%Here's how the figure was actually drawn
N=length(x);                            % length of the signal x
t=Ts*(1:N);                             % define a time vector
ssf=(-N/2:N/2-1)/(Ts*N);                % frequency vector
fx=fftshift(fft(x(1:N)));
figure(4), subplot(3,1,1), plot(ssf,abs(fx))
xlabel('magnitude spectrum at input')
fcmod=fftshift(fft(cmod(1:N)));
subplot(3,1,2), plot(ssf,abs(fcmod))
xlabel('magnitude spectrum of the oscillator')
fy=fftshift(fft(y(1:N)));
subplot(3,1,3), plot(ssf,abs(fy))
xlabel('magnitude spectrum at output')