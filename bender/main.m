% The main Bender�s decomposition program :
 
disp('Solution of stochastic 2 stage fixed recourse problem');
A = input('Enter the matrix A : ');
b = input('Enter the vector b : ');
c = input('Enter the cost vector for 1st stage problem c : ');
W = input('Enter W : ');
T = input('Enter T : ');
Q = input('Enter the vector for 2nd stage cost Q : ');
n = input('Enter the no. of scenarios n : ');
prob = input('Enter the probability for each scenario prob : ');
H = input('Enter H : ');
K = 0;L = 0;G = [];d = [];B = [];a = [];Q_x_hat = 0;beta = 0;alpha = 0;
theta_hat = -realmax;Q_x_hat = 0;flag = 1;
lb = zeros(length(c),1);
[x_hat fval_x feasible] = linprog(c,[],[],A,b,lb);
if(feasible ~= 1)
    feasible = 0;
end
stop = ~(feasible);
while(~(stop))
    z = feascut(n,W,H,T,G,d,K,x_hat);
    dim = size(z);
    if(z(1,dim(2)) == 1)
        G = z(:,1:length(c));
        d = z(:,length(c)+1);
        K = z(1,length(c)+2);
        newcut = z(1,length(c)+3);
    else
        K = z(1,dim(2)-1);
        newcut = z(1,dim(2));
    end
    K
    if(~(newcut))
        Q_x_hat = 0;
        dim1 = size(Q);
        dim2 = size(H);
        for(i = 1:n)
            if(dim1(2) > 1)
                q = Q(:,i);
            else
                q = Q;
            end
            if(dim2(2) > 1)
                h = H(:,i);
            else
                h = H;
            end
            lb = zeros(length(q),1);
            [y_hat fval_y] = linprog(q,[],[],W,h-T*x_hat,lb);
            Q_x_hat = Q_x_hat + prob(i)*fval_y;
        end
        Q_x_hat
        stop = ((abs(theta_hat - Q_x_hat) < .0001) | (theta_hat >= Q_x_hat));
        if(stop == 1)
            flag = 0;
        end
        if(~(stop))
            L = L+1;
            L
            
            beta = 0;alpha = 0;
            for(i = 1:n)
                if(dim1(2) > 1)
                    q = Q(:,i);
                else
                    q = Q;
                end
                if(dim2(2) > 1)
                    h = H(:,i);
                else
                    h = H;
                end
                
                dual_hat = linprog(-h+T*x_hat,W',q);
                beta = beta + prob(i)*(dual_hat)'*T;
                alpha = alpha + prob(i)*(dual_hat)'*h;
            end;
            B = [B;beta];
            a = [a;alpha];
        end
    end
    if(~(stop))
        t = master(K,L,A,G,B,b,d,a,c);
        if(L == 0)
            x_hat = t(1:length(t)-1);
            theta_hat = -realmax;
            stop = ~(t(length(t)));
        else
            x_hat = t(1:length(t)-2);
            theta_hat = t(length(t)-1)
            stop = ~(t(length(t)));
        end
    end
end
if(flag == 1)
    disp('The problem is not feasible');
else
    disp('The solution of the 1st stage variables is :');
    disp(x_hat);
    disp('The min. value of cost function solving by Bender Decomposition is:');
    disp(c'*x_hat+Q_x_hat);
end

