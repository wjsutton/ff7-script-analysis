# Final Fantasy VII Dialogue Word Clouds

An artistic representation of "Final Fantasy VII" dialogue, visualized through character-shaped word clouds.

[![Status](https://img.shields.io/badge/status-active-success.svg)]() [![GitHub Issues](https://img.shields.io/github/issues/user/ff7-script-analysis.svg)](https://github.com/user/ff7-script-analysis/issues) [![GitHub Pull Requests](https://img.shields.io/github/issues-pr/user/ff7-script-analysis.svg)](https://github.com/user/ff7-script-analysis/pulls) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

## :rocket: Project Overview

This project transforms the iconic dialogue of "Final Fantasy VII" characters into word clouds shaped to their silhouettes. It involves data extraction, text processing, and visual design to create a unique visualization of the game's script.

![Final Fantasy VII Word Clouds](outputs/ff7_teaser_resize.png)


## :hammer_and_wrench: Tools Used

- R for scraping the script from the web and sentiment analysis.
- Python for data preprocessing and word cloud generation.
- Figma for combineing and layingout images


## :oil_drum: Data

- Original game script scraped from: [yinza.com](https://www.yinza.com/Fandom/Script.html).
- Extracted to csv file: [FF7_dialogue_extract.csv](data/FF7_dialogue_extract.csv)
- Preprocessed and sentiment-analyzed dialogue: [FF7_dialogue_with_sentiment.csv](data/FF7_dialogue_with_sentiment.csv)

## :framed_picture: Visuals

![Final Fantasy VII Word Clouds](outputs/ff7_teaser_resize.png)

## :scroll: Scripts

- `extract_text.R`: Scrapes the game script from the provided URL.
- `text_analysis.R`: Performs sentiment analysis on the scraped script.
- `create_wordcloud.py`: Generates word clouds from the dialogue data.

## :bulb: Creating Word cloud Masks

Take FF7 character images from wikipedia pages. Generate mask with: 
[https://onlinepngtools.com/generate-png-alpha-mask](https://onlinepngtools.com/generate-png-alpha-mask)

Settings:
- Transparency Mask (α=0): rgb(255, 255, 255)
- Translucency Mask (0<α<1): rgb(0, 0, 0)
- Opacity Mask (α=1): rgb(0, 0, 0)

## :memo: License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.

---

## :memo: TO DO

- Text: tidy up and remove more stopwords
- Colours: bring sentence sentiment to influence colour
- Story add timeline to show character sentiment over time

Add to Tableau and make it interactive.

