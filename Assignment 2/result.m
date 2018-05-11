% Read the speech file that contain the noise
[x, fs]= audioread('noisy.wav');
len=length(x);
 
% Apply simple averaging which help to reduce the intensity of the high frequency
% noise if contains
    for i=1
    for j=2:len-1
    x(j,i) = (x(j-1,i) + x(j,i) + x(j+1,i))/3 ;
    end
    end
 
% Creating Gaussian window of size 20
g = gausswin(25);
 
% Apply convolution using Gaussian filter
g = g/sum(g);
y= conv(x(:,1), g, 'same');
 
% Apply signal smoothing using Savitzky-Golay smoothing filter.
result=sgolayfilt(y,1,17);
 
% resultant signal can be write to the new file
audiowrite('result.wav',result,fs);
sound(result,fs);

% plot the resultant and original signal
plot(x);title('Noisy signal');
figure; plot(result); title('Resultant signal');