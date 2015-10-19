# Part 1
#source("pollutantmean.R")
#pollutantmean("specdata", "sulfate", 1:10)
#pollutantmean("specdata", "nitrate", 70:72)
#pollutantmean("specdata", "nitrate", 23)

# Part 2
#source("complete.R")
#complete("specdata", 1)
#complete("specdata", c(2, 4, 8, 10, 12))
#complete("specdata", 30:25)
#complete("specdata", 3)

# Part 3
source("corr.R")
cr <- corr("specdata", 150)
head(cr)
summary(cr)

#cr <- corr("specdata", 400)
#head(cr)
#summary(cr)

#cr <- corr("specdata", 5000)
#summary(cr)
#length(cr)
