import nltk
nltk.download('stopwords')
nltk.download('punkt')

import pandas as pd
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

from wordcloud import WordCloud, STOPWORDS

def remove_punctuation(text):
    # Create a translation table to remove punctuation
    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    # Remove punctuation from the text
    return text.translate(translator)

# Load stopwords from nltk
stop_words = set(stopwords.words('english'))

# Function to remove stopwords
def remove_stopwords(text):
    word_tokens = word_tokenize(text)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    return ' '.join(filtered_sentence)

# Load the CSV file into a DataFrame
file_path = 'data/FF7_dialogue_with_sentiment.csv'
data = pd.read_csv(file_path)

character_list = ['cloud','tifa','barret','sephiroth','aeris','yuffie','ff7']

for character in character_list:
    print(character)

    # Filter the DataFrame for rows where Name equals 'Cloud'
    character_df = data[data['Name'].str.lower() == character].copy()

    if character == 'ff7':
        character_df = data.copy()

    # Convert the 'Line' column to lowercase
    character_df['Line'] = character_df['Line'].str.lower()

    # Apply the function to remove punctuation from the 'Line' column
    character_df['Line'] = character_df['Line'].apply(remove_punctuation)

    # Apply the function to remove stopwords from the 'Line' column
    character_df['Line'] = character_df['Line'].apply(remove_stopwords)

    # Combine all lines into a single string separated by spaces
    text_data = ' '.join(character_df['Line'].astype(str))

    # Load the mask image provided earlier
    mask_image_path = 'word_cloud_masks/' + character +'_mask.png'
    mask_image = np.array(Image.open(mask_image_path))

    # Process the mask: we want the mask's words area to be white (255) and the rest to be black (0).
    # This step might not be necessary if your mask is already in the correct format.
    mask = np.where(mask_image > 128, 255, 0).astype(np.uint8)

    # stopwords = set(STOPWORDS)
    # stopwords.add("said")

    # Generate the word cloud. Make sure 'text_data' contains your combined text as a single string.
    # wordcloud = WordCloud(background_color='white',
    #                       max_words=2000,
    #                       mask=mask,
    #                       width=1000, height=1000,
    #                       stopwords=stopwords,
    #                       contour_width=2,
    #                       contour_color='black')

    wordcloud = WordCloud(background_color='black',
                        max_words=2000,
                        margin=0,
                        min_font_size=1,
                        color_func=lambda *args, **kwargs: (128, 128, 255),
                        font_path='fonts\BentonSans Regular Regular.otf',
                        prefer_horizontal=0.7,
                        mask=mask,
                        width=1000, height=1000,
                        contour_width=5,
                        scale = 10,
                        contour_color='#444487')

    wordcloud.generate(text_data)

    # store to file
    wordcloud.to_file('wordclouds/' + character + ".png")

    df = pd.DataFrame(wordcloud.layout_, columns = ['Name', 'Sive', 'Coord', 'Direction','Color'])
    df.to_csv('coords/' + character + '_coordinates.csv')
