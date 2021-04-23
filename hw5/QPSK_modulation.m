% String for testing
test_str='EC415';

% Get QPSK symbols;
QPSK_symbols=letters2QPSK(test_str);

time=8*length(test_str); Ts=1/1000; % sampling interval & time
t=Ts:Ts:time; lent=length(t);       % define a time vector
w=zeros(1,lent);
start=0;
for i=1:time/2
    w((2*start/Ts)+1:i*2/Ts)=QPSK_symbols(i);
end


fm=1; fc=10; c=exp(j*2*pi*fc*t);   % carrier at freq fc

%w=5/lent*(1:lent)+cos(2*pi*fm*t);   % create "message"
%w
v=c.*w;                             % modulate with carrier

% used to plot figure
subplot(2,1,1), plot(t,w)
axis([0,time, -1,3])
ylabel('amplitude'); xlabel('time'); title('(a) message signal');
subplot(2,1,2), plot(t,v)
axis([0,time, -2.5,2.5])
ylabel('amplitude'); xlabel('time'); title('(b) message after modulation');