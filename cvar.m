[~,assetName] = xlsread('D:\Cabaza\matlab\fiveData\monthlymeanSeries5.csv','B1:F1') % 1 * matrix %
e=xlsread('D:\Cabaza\matlab\fiveData\monthlymeanSeries5.csv','B2:F2'); % 1 * matrix %
sigma=xlsread('D:\Cabaza\matlab\fiveData\monthlyvarianceSeries5.csv','B2:F6');  % 50 * 50 matrix %
n = length(e);
p = PortfolioCVaR;
p = setAssetList(p,assetName);
AssetScenarios = mvnrnd(e, sigma, 20000);
p = setScenarios(p, AssetScenarios);

p = setDefaultConstraints(p);
disp(p);
p = setProbabilityLevel(p,0.85);
plotFrontier(p);

pwgt = estimateFrontier(p, 1);
pnames = cell(1,1);
pnames{1} = sprintf('Optimal Portfolio',1);
Blotter = dataset([{pwgt},pnames],'obsnames',p.AssetList);
disp(Blotter);

pret = estimatePortReturn(p, pwgt);
disp(pret);
