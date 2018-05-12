mean = xlsread('C:\Users\HP\PycharmProjects\MiniProject\monthlymeanSeries5.csv','B2:F2');
variance = xlsread('C:\Users\HP\PycharmProjects\MiniProject\monthlyvarianceSeries5.csv','B2:F6');
[one, num_assets] = size(mean);
disp(num_assets)
cases = 10;
rng default  % For reproducibility global R
R = mvnrnd(mean, variance, cases);
global lending_interest_rate
lending_interest_rate = 1;
global borrowing_interest_rate
borrowing_interest_rate = 10;
global required_wealth
required_wealth = 1.00;
global current_wealth
current_wealth = 1.01;
disp(size(R))
cvx_begin
    variable x(num_assets)
    z = 0;
    for i = 1:cases
        %z = z - (1 + lending_interest_rate) * min((-R(i,:)*x + required_wealth), 0) + (1 + borrowing_interest_rate) * min((R(i,:)*x - required_wealth), 0);
        %z = z + (1 + lending_interest_rate) * (R(i,:)*x - required_wealth) + ( - borrowing_interest_rate + lending_interest_rate) * min(R(i,:)*x - required_wealth, 0);
        z = z + min((1 + lending_interest_rate) * (R(i,:)*x - required_wealth), (1 + borrowing_interest_rate) * (R(i,:)*x - required_wealth))
    end
    z = z/cases
    disp(z);
    maximize(z)
    subject to
        sum(x) == current_wealth
        x >= 0
cvx_end
