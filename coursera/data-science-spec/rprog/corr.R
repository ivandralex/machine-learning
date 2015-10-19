corr <- function(directory, threshold = 0) {
  correlations <- numeric(0)
  files <- list.files(directory)
  len <- length(files)
  for(i in 1:len) {
    path <- file.path(directory, files[i])
    data <- read.csv(path)
    
    good <- complete.cases(data)
    sublist <- data[good,]
    
    if(dim(sublist)[1] > threshold){
      correlations <- c(correlations, cor(sublist['sulfate'], sublist['nitrate']))
    }
  }
  
  correlations
}