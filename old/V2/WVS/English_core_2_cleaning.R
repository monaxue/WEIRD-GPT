library(stringr)

data <- read.csv("English_core_2_v3_run_1_cleaned.csv")

for (i in 1:nrow(data)){
  numbers <- as.numeric(str_extract_all(data[i,1], "\\d+\\.?\\d*")[[1]])
  name <- paste("core_2_", numbers, sep = "")
  data[i, name] <- 1 #mentioned
  data[i,is.na(data[i,])] <- 2
}

data <- data[2:ncol(data)]


write.csv(data, file = "English_core_2_v3_run_1_cleaned_2.csv", row.names = FALSE)
