pollutantmean <- function(directory, pollutant, id = 1:332) {
  pollutantList <- list()
  files <- list.files(directory)
  for(i in id) {
    path <- file.path(directory, files[i])
    data <- read.csv(path)
    
    sublist <- data[, pollutant]
    good <- complete.cases(sublist)
    sublist <- sublist[good]
    pollutantList <- append(pollutantList, sublist)
  }
  
  mean(sapply(pollutantList, mean))
}
