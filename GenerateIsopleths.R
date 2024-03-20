  library("lattice")
  library(MASS)
  library(autoimage)
  require(akima)
  library(ggplot2)
  library(tidyverse)
  
  # Init Conditions
  InitialCondition1 = 'CH4'
  InitialCondition2 = 'NO'
  InitialCondition3 = 'NO2'
  InitialCondition4 = 'CH4'
  TestCondition = 'O3'
  
  # Load File Location
  files = list.files('C:\\Users\\Josh\\Downloads\\MCM_CO_CH4_output_files_test' , full.names=TRUE)
  
  
  InitialCondition1Vector = c()
  InitialCondition2Vector = c()
  TestConditionVector = c()
  
  for (x in files) {
    runOutput <- read.csv(x, sep = "")
    # InitialCondition1Vector <- c(InitialCondition1Vector, runOutput[1,InitialCondition1] + runOutput[1,InitialCondition4])
    # InitialCondition2Vector <- c(InitialCondition2Vector, runOutput[1,InitialCondition3] + runOutput[1,InitialCondition2])
    InitialCondition1Vector <- c(InitialCondition1Vector, runOutput[1,InitialCondition1])
    InitialCondition2Vector <- c(InitialCondition2Vector, runOutput[1,InitialCondition3] + runOutput[1,InitialCondition2])
    
    TestConditionVector <- c(TestConditionVector, max(runOutput[TestCondition]))
    # TestConditionVector <- c(TestConditionVector, runOutput[1, TestCondition])
  }
  
  x=c(InitialCondition1Vector)
  y=c(InitialCondition2Vector)
  O3Conc=c(TestConditionVector)
  
  
  # This scales all the numbers to be several magnitudes larger to avoid akima interpolation
  # from failing to interpolate between tiny numbers
  x <- x 
  y <- y 
  O3Conc <- O3Conc
  
  x <- x
  y <- y
  O3Conc <- O3Conc
  
  data <- data.frame(x, y, O3Conc)
  # Note: This resolution changes how much you want to interpolate between dots.
  # Try to keep this as large as possible to avoid sucking up all the ram
  resolution <- 100000000000
  
  a <- interp(x=data$x, y=data$y, z=data$O3Conc, 
              xo=seq(min(data$x),max(data$x),by=resolution), 
              yo=seq(min(data$y),max(data$y),by=resolution), duplicate="mean")
  
  a$x <- a$x 
  a$y <- a$y 
  a$z <- a$z 
  
  
  image(a, useRaster=TRUE)
  
  dataInterp <- data.frame(a$z)
  write.csv(data, "data.csv", row.names=FALSE)
  autopoints(InitialCondition1Vector, InitialCondition2Vector, TestConditionVector,
              xlab = InitialCondition1, ylab = InitialCondition2, n = 100)
  
  contour(a$x , a$y ,a$z)
