mean = xlsread('C:\Users\HP\PycharmProjects\MiniProject\monthlymeanSeries5.csv','B2:F2')
variance = xlsread('C:\Users\HP\PycharmProjects\MiniProject\monthlyvarianceSeries5.csv','B2:F6')
[one, num_assets] = size(mean)
variance_limit = 0.01
disp(num_assets)
W = 1
cvx_begin
    variable x(num_assets)
    maximize( mean*x )
    subject to
       sum(x)== W
       transpose(x) * variance * x <= variance_limit
       x >= zeros(num_assets, 1)
cvx_end
