# Measurement Converter 

Uses selenium, beautiful soup, and pandas
Goal: Take a webpage's measurements and convert to user's selected type (whether metric-> imperial or imperial-> metric).

Step 1 is to convert the text - > the browser extension will parse the webpage, I believe by using beautiful soup
The text is saved? by beautiful soup and will need to be converted to the alternative. So in order to do that, 
we need to determine if the unit we received was in metric or imperial units. 
Then we need to convert that unit that was highlighted. We can use the pandas library for this. 
So now we have a converted unit. Our browser app should populate the most recent data that we converted from our pandas 
library **Ancillary but cool** figure out how to have the conversion appear when you right click
