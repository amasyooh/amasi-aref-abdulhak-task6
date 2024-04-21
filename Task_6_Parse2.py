from bs4 import BeautifulSoup
def update_image_source(html_content, new_image_path):
# Parse the HTML content
soup
BeautifulSoup (html_content, 'html.parser')
# Find the <img> tag by its id
logo img = soup.find('img', {'id': 'logo'})
if logo_img:
else:
# Update the 'src' attribute with the new image path
logo_img['src'] = new_image_path
print("Image source updated.")
print("No image found with the specified id.")
# Convert the soup object back to a string
updated_html = str(soup)
return updated_html
# Example HTML content
html content = ***
<html>
<head></head>
<body>
<img id="logo" src="old_logo.png">
</body>
</html>
# New image path
new_image_path = 'new_logo.png'
# Update the image source
updated_html = update_image_source(html_content, new_image_path)
print("Updated HTML:")
print (updated_html)
