library(rvest)
library(dplyr)
library(stringr)


index_url <- "https://www.yinza.com/Fandom/Script.html"

# Read the HTML content
html_data <- read_html(index_url)

# Extract <a> tags
links <- html_data %>%
  html_elements("a")

# Extract href attributes and text
link_data <- data.frame(
  Href = links %>% html_attr("href"),
  Text = links %>% html_text()
)

link_data$link_page <- as.integer(substr(link_data$Href,8,9))
link_data <- filter(link_data,!is.na(link_page))
link_data$page_url <- paste0('https://www.yinza.com/Fandom/Script/',substr(link_data$Href,8,9),'.html')

total_pages <- nrow(link_data)
results <- list()

for(i in 1:total_pages){
  Sys.sleep(30)
  
  print("Working on...")
  print(paste0("Page: ",i))
  print(paste0("URL: ",link_data$page_url[i]))
  print(paste0("Page: ",link_data$Text[i]))

  # Load the HTML content from the website
  url <- link_data$page_url[i]
  page <- read_html(url)
  
  # Extract dialogue blocks with HTML content
  dialogue_blocks <- page %>%
    html_elements("p.indent") 
  
  # Process each block to extract name and dialogue
  dialogues <- lapply(dialogue_blocks, function(html_block) {
    # Extract the name using regex to get content inside <b></b>
    name <- str_extract(html_block, "(?<=<b>)[^<]+")
    # Extract dialogue by removing the name and HTML tags, then cleaning up
    dialogue <- html_block %>%
      str_remove(pattern = paste0("<b>", name, "</b><br/>")) %>%
      str_remove_all("<[^>]+>") %>%
      str_trim()
    
    data.frame(Name = name, Line = dialogue)
  })
  
  # Combine all dialogues into a single dataframe
  dialogue_df <- bind_rows(dialogues)
  
  dialogue_df$Line <- substr(dialogue_df$Line,nchar(dialogue_df$Name)+1,nchar(dialogue_df$Line))
  dialogue_df$source <- url
  dialogue_df$section <- link_data$Text[i]
  dialogue_df$section_order <- as.integer(substr(link_data$Href[i],8,9))
  
  results[[i]] <- dialogue_df

}

game_dialogue_df <- bind_rows(results)

# Write the results to a CSV file
write.csv(game_dialogue_df, "data/FF7_dialogue_extract.csv", row.names = FALSE, quote = TRUE)

# Print a message when done
cat("CSV file created")
