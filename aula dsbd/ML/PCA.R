dados <- read.table("https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data",
                    sep = ",")

tipo <- dados$V1
table(tipo)
VARS <- dados[,-1]

apply(VARS, 2, sd)
pairs(VARS[,1:3], col= tipo, cex=2)
require(rgl)
plot3d(VARS[,1:3], col=tipo)

ACP <- prcomp(VARS, scale=TRUE)

#dados das componentes
nrow(ACP$x)
nrow(VARS)

#2d
prop <- round((ACP$sdev[1:2]^2)/sum(ACP$sdev^2), 4) *100
plot(ACP$x[,1], 
       ACP$x[,2],
       col=tipo,
       cex=2,
       pch=19,
       ylab = prop[1],
       xlab = prop[2])

#3d
prop <- round((ACP$sdev[1:3]^2)/sum(ACP$sdev^2), 4) *100
plot3d(ACP$x[,1], 
     ACP$x[,2],
     ACP$x[,3],
     col=tipo,
     size = 8, 
     ylab = prop[1],
     xlab = prop[2],
     zlab = prop[3])

#Analise de componentes PCA
ACP$rotation
