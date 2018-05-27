function [X]=DFT_nik(x)

N=length(x);
for k=1:N
    X(k)=0;
    for n=1:N
        X(k)=X(k)+x(n).*exp(-1j.*2.*pi.*(n-1).*(k-1)./N);
    end
end

f=0:N-1;
subplot(311)
stem(0:N-1,x)
title('Sequence x (in time domain)')
xlabel('time')
ylabel('Amplitude')
grid;

subplot(323)
stem(f,abs(X))
title('Magnitude of Fourier Coeffients using function')
ylabel('|X|')
grid;

subplot(325)
stem(f,angle(X))
title('Angle of Fourier Coeffients using function')
xlabel('Frquency coefficients')
ylabel('<X')
grid;

subplot(324)
stem(f,abs(fft(x)))
title('Magnitude of Fourier Coeffients using fft function')
ylabel('|X|')
grid;

subplot(326)
stem(f,angle(fft(x)))
title('Angle of Fourier Coeffients using fft function')
xlabel('Frquency coefficients')
ylabel('<X')
grid;
