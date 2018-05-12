e=xlsread('D:\Cabaza\matlab\fiveData\monthlymeanSeries5.csv','B2:F2'); % 1 * matrix %
n = length(e);
sigma=xlsread('D:\Cabaza\matlab\fiveData\monthlyvarianceSeries5.csv','B2:F6');  % 50 * 50 matrix %
W=1; % Initial total wealth to invest %
b = 1; % atleast b wealth with probability 'alpha' after return %
alpha=0.1;
T = cholcov(sigma); %cholesky like decomposition s.t. sigma = T * T.'%
cvx_begin
    variable x(n)
    maximize( e*x )    % maximize expected return %
    subject to
        sum(x)== W               % total wealth %
        b - e*x + (norminv(1-alpha,0,1) * norm((T.' * x),2)) <= 0
        x >= zeros(n, 1)             
cvx_end
