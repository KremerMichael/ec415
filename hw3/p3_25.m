% Set UP
n = 100;
alphabet = [3, 1, 1, 3];

% For A and B
x = randn(1,n);
y = quantalph (x , alphabet );

% Get percentages of 1 & 3
num1=0; num3=0;
for i=1:n
    
    if y(i) == 1
        num1 = num1 + 1;
    elseif y(i) == 3
        fprintf('trig\n')
        num3 = num3 + 1;
    end
end
fprintf(' 1 appered %d percent of the time\n', num1/n*100)
fprintf(' 3 appered %d percent of the time\n', num3/n*100)

% Plot
plotspec(x,1)

% For c
x = 3*randn(1, n);
y = quantalph (x , alphabet );

% Get percentages of 1 & 3
num1=0; num3=0;
for i=1:n
    if y(i) == 1
        num1 = num1 + 1;
    elseif y(i) == 3
        num3 = num3 + 1;
    end
end
fprintf(' 1 appered %d percent of the time\n', num1/n*100)
fprintf(' 3 appered %d percent of the time\n', num3/n*100)

% Plot