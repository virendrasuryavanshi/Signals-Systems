[x,fs] = audioread('part_22.wav');
%sound(x,fs);
%function [X]=DFT_nik(x)
N=length(x);
f=0:N-1;
subplot(211)
plot(0:N-1,x)
title('Sequence x (in time domain)')
xlabel('time')
ylabel('Amplitude')
grid;

N=length(x);
f=0:N-1;
subplot(212)
plot(f,abs(fft(x)))
title('Magnitude of Fourier Coeffients using fft function')
ylabel('|X|')
grid;

