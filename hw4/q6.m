load('qam_hw(1).mat','v')

time=0.3; Ts=1/10000;               % sampling interval & time
t=Ts:Ts:time; lent=length(t);       % define a time vector

fc=1000;
gam=0; phi=0;                       % freq & phase offset
c1=cos(2*pi*(fc+gam)*t+phi);        % create cosine for demod
c2=sin(2*pi*(fc+gam)*t+phi);        % create sine for demod

x1=v.*c1;                            % demod received signal
x2=v.*c2;                            % demod received signal

fbe=[0 0.1 0.2 1]; damps=[1 1 0 0]; % LPF design
fl=100; b=firpm(fl,fbe,damps);      % impulse response of LPF
m1=2*filter(b,1,x1);                % LPF the demodulated signal
m2=2*filter(b,1,x2);                % LPF the demodulated signal

% used to plot figure
figure(1)
axis([0,0.3, 11,11.1])
ylabel('amplitude'); 
title('message after modulation');
subplot(1,1,1), plot(t,v)

figure(2)
subplot(2,1,1), plot(t,x1)
axis([0,0.3, -1,10])
ylabel('amplitude');
title('demodulated signal x1');
subplot(2,1,2), plot(t,m1)
axis([0,0.3, -1,10])
ylabel('amplitude'); title('recovered message is a LPF applied to x1');

figure(3)
subplot(2,1,1), plot(t,x2)
axis([0,0.3, -10,1])
ylabel('amplitude');
title('demodulated signal x2');
subplot(2,1,2), plot(t,m2)
axis([0,0.3, -10,1])
ylabel('amplitude'); title('recovered message is a LPF applied to x2');