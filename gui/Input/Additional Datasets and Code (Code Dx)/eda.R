library(readr)
atom_file <- read_csv("Northeastern University/Q8_Fall2023/Project/Sample code and input/Additional Datasets and Code (Code Dx)/atom (30 May 2020).csv")

View(atom_file)

barplot(atom_file$Type)

atom_Type_freq <- table(atom_file$Type)

barplot(atom_Type_freq,
        main = "Bar Plot of Frequency of Type",
        xlab = "Type",
        ylab = "Frequency",
        col = "skyblue", # Bar color
        horiz = TRUE
)
