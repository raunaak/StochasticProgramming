% Function to solve the master problem :

function z = master(K,L,A,G,B,b,d,a,c)
if (L > 0)
    if(K > 0)
        Z = [A zeros(length(b),1) zeros(length(b),1);...
       -A zeros(length(b),1) zeros(length(b),1);...
       -G zeros(K,1) zeros(K,1);...
       -B -ones(L,1) ones(L,1)];
        p = [b;-b;-d;-a];
    else
        Z = [A zeros(length(b),1) zeros(length(b),1);...
       -A zeros(length(b),1) zeros(length(b),1);...
       -B -ones(L,1) ones(L,1)];
        p = [b;-b;-a];
    end
    c_new = [c' 1 -1]';
    lb = zeros(length(c_new),1);
    [values,fval,exitflag] = linprog(c_new,Z,p,[],[],lb);
    if(exitflag ~= 1)
        exitflag = 0;
    end
    theta_hat = values(length(values)-1) - values(length(values));
    z = [(values(1:length(values)-2));theta_hat;exitflag];
else
    Z = [A;-A;-G];
    p = [b;-b;-d];
    lb = zeros(length(c),1);
    [values,fval,exitflag] = linprog(c,Z,p,[],[],lb);
    if(exitflag ~= 1)
        exitflag = 0;
    end
    z = [values;exitflag];
end
end
