mean = xlsread('C:\Users\HP\PycharmProjects\MiniProject\monthlymeanSeries5.csv','B2:F2')
variance = xlsread('C:\Users\HP\PycharmProjects\MiniProject\monthlyvarianceSeries5.csv','B2:F6')
[one, num_assets] = size(mean)
disp(num_assets)
W = 1
minimum_portfolio_value = 1.01
cvx_begin
    variable x(num_assets)
    minimize( transpose(x) * variance * x )
    subject to
       sum(x)== W
       mean * x >= minimum_portfolio_value
       x >= zeros(num_assets, 1)
cvx_end
