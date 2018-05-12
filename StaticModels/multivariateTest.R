MyData <- read.csv(file="C:/Users/HP/PycharmProjects/MiniProject/monthlyreturnPrices5.csv", header=TRUE, sep=",", colClasses=c("NULL",NA,NA,NA,NA,NA))
#print(MyData)
#library(energy)
#mvnorm.etest(MyData, R = 83)

library(ICS)
mvnorm.kur.test(MyData)
mvnorm.skew.test(MyData)
