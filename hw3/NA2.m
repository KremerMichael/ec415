T = 1;                   % Total time
F1 = 1/T;                % Fundamental frequency
fs = 256;                % Assumed sample frequency
N = fs*T;                % Calculate number of points
M = 21;                  % Number of coefficients
t = (1:N)*T/N;           % Generate time vector
f = (0:M)*fs/N;          % and frequency vector for plotting
%x = [t(1:N/2) zeros(1,N/2)];   % Generate signal, ramp followed by zeros

x = 3*randn(1, N);
alphabet = [3, 1, 1, 3];
y = quantalph (x , alphabet );

%
Xf = fft(y);            % Take Fourier transform, scale
Mag = abs(Xf)*2/N;        % Normalize
Phase = -angle(Xf)*360/(2*pi);
%
plot(f(1:M),Mag(1:M),'.'); hold on; % Plot only first 20 coefficients plus DC