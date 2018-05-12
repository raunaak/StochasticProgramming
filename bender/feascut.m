%Function to find the feasibility cut :

function z = feascut(script_A,W,H,T,G,d,K,x_hat)
newcut = 0;
i = 1;
while((i <= script_A) && (newcut == 0))
    dim2 = size(H);
    if(dim2(2) > 1)
        h = H(:,i);
    else
        h = H;
    end
    r = size(W);
    m = r(1);
    n = r(2);
    Z = [W' -W';ones(1,m) ones(1,m)];
    p = [zeros(n,1);1];
    c = [-(h-T*x_hat);(h-T*x_hat)];
    [values fval] = linprog(c,Z,p,[],[],zeros(2*m,1));
    newcut = (fval < 0);
    if(newcut)
        K = K+1;
        sigma = values(1:m)-values((m+1):2*m);
        G = [G;sigma'*T];
        d = [d;sigma'*h];
    end
    i = i+1;
 end
w = length(d)-1;
w1 = [K;zeros(w,1)];
w2 = [newcut;zeros(w,1)];
z = [G d w1 w2];
end