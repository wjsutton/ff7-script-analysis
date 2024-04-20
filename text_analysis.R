library(syuzhet)
library(dplyr)
library(tidyr)
library(readr)

file_path <- "data/FF7_dialogue_extract.csv"
df <- read_csv(file_path)

# Tidy up data and remove duplicated lines
df <- filter(df,!is.na(df$Line))
df_unique <- unique(df)

# Applying sentiment analysis on each row of the DIALOGUE column
df_sentiment <- df %>%
  rowwise() %>%
  mutate(sentiment_list = list(get_nrc_sentiment(Line))) %>%
  ungroup()

# Unnest the sentiment list into separate columns
df_sentiment_expanded <- df_sentiment %>%
  tidyr::unnest_wider(col = sentiment_list)

# Write to CSV
output_path <- "data/FF7_dialogue_with_sentiment.csv"
write_csv(df_sentiment_expanded, output_path)

