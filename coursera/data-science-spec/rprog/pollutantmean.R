pollutantmean <- function(directory, pollutant, id = 1:332) {
  pollutantList <- list()
  files <- list.files(directory)
  for(i in id) {
    path <- file.path(directory, files[i])
    data <- read.csv(path)
    
    sublist <- data[, pollutant]
  }
  
  print(sublist)
}

