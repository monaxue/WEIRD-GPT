library(stringr)


main_run1 <- read.csv("English_main_questions_v3_run_1.csv")
main_run2 <- read.csv("English_main_questions_v3_run_2.csv")


main <- rbind(main_run1, main_run2)
unique_main <- apply(main, 2, unique)

main[98, "happiness_4"] <- NA

main <- apply(main, 2, function(x) as.numeric(str_replace_all(x, "[^0-9.]", "")))

nas_indices <- which(is.na(main), arr.ind = TRUE)

core_2_run1 <- read.csv("English_core_2_v3_run_1_cleaned_2.csv")
core_2_run2 <- read.csv("English_core_2_v3_run_2_cleaned_2.csv")

core_2 <- rbind(core_2_run1, core_2_run2)

df <- cbind(cbind(main[, 1:6], core_2), main[,7:241])

write.csv(df, file = "English_all_questions_v3.csv", row.names = FALSE)


