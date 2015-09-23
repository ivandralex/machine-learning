complete <- function(directory, id = 1:332) {
  completeCases <- data.frame(id=numeric(), nobs=numeric())
  files <- list.files(directory)
  for(i in id) {
    path <- file.path(directory, files[i])
    data <- read.csv(path)
    
    good <- complete.cases(data)
    sublist <- data[good,]
    
    completeCases <- rbind(completeCases, data.frame(id=sublist[1, 'ID'], nobs=dim(sublist)[1]))
  }
  
  completeCases
}
