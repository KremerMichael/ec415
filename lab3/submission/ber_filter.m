% open bin file
a = fopen('ask_out.bin');
b = fread(a);

% what good values should be
good = [1; 1; 0; 1; 0];
j=1; % for iterating into above vector

% for counting error
err=0;
total = 9999-4;

% start after first bit error at index 5
for i=5:9999
    %if error
    if b(i) ~= good(j)
        err=err+1;
    end
    %loop index for vector "good"
    if j == 5
        j = 1;
    else
        j=j+1;
    end
end
    
%print results
fprintf("The BER is %d/%d=%f\n",err, total, err/total)