p = 0.5;
assets = 2;
cases = 2;
timePeriod = 4;
childPerNode = 2;
nodes = power(2, timePeriod) - 1;
initialWealth = 60;
targetWealth = 80;
prob = power(p, timePeriod - 1);
randomReturn = zeros(cases, assets);
randomReturn(1, 1) = 1.25; 
randomReturn(1, 2) = 1.14;
randomReturn(2, 1) = 1.06;
randomReturn(2, 2) = 1.12;
g = 0.2;
r = 50;
cvx_begin
    variable x(nodes, assets)
    variable y(nodes)
    variable wplus(nodes)
    variable wminus(nodes)
    z = 0;
    for i = power(2, timePeriod - 1) : power(2, timePeriod) - 1
        z = z + prob * (g * wplus(i) - r * wminus(i));
    end
    maximize(z)
    subject to
        y == sum(x, 2);
        y(1) == initialWealth;
        for i=1:floor(nodes/4)
            randomReturn(1, :) * transpose(x(i, :)) - y(2 * i) == 0;
            randomReturn(2, :) * transpose(x(i, :)) == y(2 * i + 1);
        end
        for i = power(2, timePeriod - 2): power(2, timePeriod - 1) - 1
            randomReturn(1, :) * transpose(x(i, :)) == targetWealth + wplus(2*i) - wminus(2*i);
            randomReturn(2, :) * transpose(x(i, :)) == targetWealth + wplus(2*i + 1) - wminus(2*i + 1);
        end
        x >= 0;
        wplus >= 0;
        wminus >= 0;
cvx_end