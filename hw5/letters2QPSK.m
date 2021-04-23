% function complex_out = qpsk_enc(m)
%     M=4;
%     complex_out = exp(j*2*pi*(m-1)/M);
% end

function out = letters2QPSK(str) % call as Matlab function

% Convert ascii to binary string
binary=dec2bin(str);
[l, w] = size(binary);
bin="";
for i=1:l
    row="0"+binary(i:i,:);
    bin=bin+row;
end
bin=char(bin);

% Convert binary string to stuff
out = zeros(1,4*length(str));
M=4;
indx=1;
for i=1:2:length(bin)
    if bin(i) == '0'
        if bin(i+1) == '0'
            m=1;
        else
            m=2;
        end
    else
        if bin(i+1) == '0'
            m=4;
        else
            m=3;
        end
    end
    out(indx)= exp(j*2*pi*(m-1)/M);
    indx=indx+1;
end

