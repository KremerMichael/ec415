header=[1 -1 1 -1 -1 1 1 1 -1 -1];     % header is a predefined string
loc=30; r=25;                          % place header in position loc


sd=[0 0.1 0.3 0.5 1 2];

for i=1:1:length(sd)
    data=[sign(randn(1,loc-1)) header sign(randn(1,r))];  % generate signal
    data=data+sd(i)*randn(size(data));              % add noise
    y=xcorr(header, data);                 % do cross correlation
    [m,ind]=max(y);                        % location of largest correlation
    headstart=length(data)-ind+1;          % place where header starts
    figure(i)
    subplot(3,1,1), stem(header)           % plot header
    title('Header')
    subplot(3,1,2), stem(data)             % plot data sequence
    title('Data with embedded header (sd='+string(sd(i))+')')
    subplot(3,1,3), stem(y)                % plot correlation
    title('Correlation of header with data (sd='+string(sd(i))+')')
end