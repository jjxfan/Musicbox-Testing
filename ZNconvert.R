# Load necessary libraries
library(dplyr)
library(readr)

# Define the folder containing the output files
input_dir <- "C://Users//Josh//Downloads//ZNoutput"
output_file <- "C://Users//Josh//Downloads//summary_output.csv"

files <- list.files(input_dir, pattern = "*.csv", full.names = TRUE) # Assuming the files have a .txt extension

# Initialize an empty list to store data from each file
data_list <- list()

# Loop through each file
for (file in files) {
  # Read the file with multi-space as delimiter
  data <- read.table(file, header = TRUE, sep = "", strip.white = TRUE)
  
  # Process each Z/N pair and calculate dCompound
  compounds <- c("NO", "NO2", "HNO3") # Extend this vector based on your compounds
  for (compound in compounds) {
    n_compound <- compound
    z_compound <- sub("N", "Z", n_compound, fixed = TRUE)
    ratio <- data[[z_compound]] / data[[n_compound]]
    d_compound <- 1000 * (ratio / 0.0034 - 1)
    # Set dCompound to zero for N compound < 10^5
    d_compound[data[[n_compound]] < 1e5] <- 0
    # Add the dCompound column to data
    data[[paste0("d", compound)]] <- d_compound
  }
  
  # Calculate max and min of dCompound for each pair and their times
  # Assuming you have a 'Time' column in your data
  summary_data <- c()
  for (compound in compounds) {
    d_compound_col <- paste0("d", compound)
    summary_data[paste0(d_compound_col, "max")] = max(data[[d_compound_col]], na.rm = TRUE)
    summary_data[paste0("t", d_compound_col, "max")] <- data$t[which.max(data[[d_compound_col]])]
    summary_data[paste0(d_compound_col, "min")] <- min(data[[d_compound_col]], na.rm = TRUE)
    summary_data[paste0("t", d_compound_col, "min")] <- data$t[which.min(data[[d_compound_col]])]
    summary_data[paste0("init", d_compound_col)] <- data[1, compound]
  }
  
  summary_data[paste0("initCO")] <- data[1, "CO"]
  summary_data[paste0("initCH4")] <- data[1, "CH4"]
  summary_data[paste0("O3", "max")] = max(data["O3"], na.rm = TRUE)
  summary_data[paste0("t", "O3", "max")] <- data$t[which.max(data[["O3"]])]
  
  
  
  # Append the summary data to the list
  data_list[[file]] <- summary_data
}

# Combine all summaries into a single data frame
final_summary <- df <- do.call(rbind, lapply(data_list, function(x) as.data.frame(t(as.data.frame(x)))))


# Write the final summary to an output file
write.csv(final_summary, output_file, row.names = TRUE)
