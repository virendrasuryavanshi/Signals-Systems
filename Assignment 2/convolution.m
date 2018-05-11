prompt1 = 'Enter First signal';
x = input(prompt1);
prompt2 = 'Enter Second Signal ';
h = input(prompt2);
y=conv(x,h,'full');
disp(y);

plot(x); stem(x);title('First signal');
figure;plot(h); stem(h);title('Second signal');
figure;plot(y); stem(y);title('Convolved signal');

