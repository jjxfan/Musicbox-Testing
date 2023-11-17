library("lattice")
library(MASS)
library(autoimage)
require(akima)
library(ggplot2)
library(tidyverse)

# Init Conditions
InitialCondition1 = 'CONC.RH'
InitialCondition2 = 'CONC.NO2'
TestCondition = 'CONC.O3'

# Load File Location
folderLocation = 'C:\\Users\\Josh\\Downloads\\outputFiles500'
file_namespart1 <- c()

# file_namespart1 <- c(file_namespart1, paste0('C:\\Users\\Josh\\Downloads\\outputFiles\\my_config', '0', 0:9, '.csv'))
# file_namespart2 <- c(file_namespart1, paste0('C:\\Users\\Josh\\Downloads\\outputFiles\\my_config', '00', 0:9, '.csv'))
file_namespart3 <- paste0('C:\\Users\\Josh\\Downloads\\outputFiles500\\my_config_', 1:499, '.csv') # Change the 499 to the largest file name number


file_names <- paste0('C:\\Users\\Josh\\Downloads\\outputFiles500\\my_config_', 10:49, '.csv')
file_names <- c(file_namespart3, file_names)

InitialCondition1Vector = c()
InitialCondition2Vector = c()
TestConditionVector = c()

for (x in 1:439) { # change the 439 to the largest file name number
  runOutput <- read.csv(file_namespart3[x])
  InitialCondition1Vector <- c(InitialCondition1Vector, runOutput[1,InitialCondition1])
  InitialCondition2Vector <- c(InitialCondition2Vector, runOutput[1,InitialCondition2])
  TestConditionVector <- c(TestConditionVector, max(runOutput[TestCondition]))
}

x=c(InitialCondition1Vector)
y=c(InitialCondition2Vector)
O3Conc=c(TestConditionVector)


# This scales all the numbers to be several magnitudes larger to avoid akima interpolation
# from failing to interpolate between tiny numbers
x <- x * 1000000
y <- y * 1000000
O3Conc <- O3Conc * 1000000

x <- x
y <- y
O3Conc <- O3Conc

data <- data.frame(x, y, O3Conc)
# Note: This resolution changes how much you want to interpolate between dots.
# Try to keep this as large as possible to avoid sucking up all the ram
resolution <- 1

a <- interp(x=data$x, y=data$y, z=data$O3Conc, 
            xo=seq(min(data$x),max(data$x),by=resolution), 
            yo=seq(min(data$y),max(data$y),by=resolution), duplicate="mean")

a$x <- a$x / 1000000
a$y <- a$y / 1000000
a$z <- a$z / 1000000


image(a, useRaster=TRUE)

dataInterp <- data.frame(a$z)
write.csv(data, "data.csv", row.names=FALSE)
autopoints(InitialCondition1Vector, InitialCondition2Vector, TestConditionVector,
            xlab = InitialCondition1, ylab = InitialCondition2)

contour(a$x , a$y ,a$z)
