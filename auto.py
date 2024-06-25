import os

# Paths to the folders containing certification images
fulls_folder = 'C:/Users/mahav/OneDrive/Desktop/Portfolio/images/fulls'
thumbs_folder = 'C:/Users/mahav/OneDrive/Desktop/Portfolio/images/thumbs'
html_file = '"C:/Users/mahav/OneDrive/Desktop/Portfolio/certification.html"'

# Function to generate HTML for the images
def generate_html(fulls_folder, thumbs_folder):
    # Start with the HTML structure
    html = """
<!DOCTYPE HTML>
<html>
<head>
    <title>Certifications</title>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="stylesheet" href="assets/css/main.css" />
</head>
<body>
    <div id="wrapper">
        <header id="header">
            <h2><em>Certifications from different online learning platforms, other workshops and hackathons held in college as well as social work done during my 4 year Undergrad</em></h2>
        </header>
        <section id="main">
            <section class="thumbnails">
"""
    # Dictionary to map thumbnails to full images
    images = {}

    # Populate the dictionary with filenames from the fulls folder
    for filename in os.listdir(fulls_folder):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            name_without_ext = os.path.splitext(filename)[0]
            images[name_without_ext] = {'full': filename, 'thumb': None}

    # Match thumbnails to the dictionary
    for filename in os.listdir(thumbs_folder):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            name_without_ext = os.path.splitext(filename)[0]
            if name_without_ext in images:
                images[name_without_ext]['thumb'] = filename

    # Generate HTML for each image
    div_counter = 0
    for image_name, paths in images.items():
        if paths['thumb'] and paths['full']:
            if div_counter % 8 == 0:
                if div_counter > 0:
                    html += '        </div>\n'
                html += '        <div>\n'
            html += f"""
            <a href="images/fulls/{paths['full']}">
                <img src="images/thumbs/{paths['thumb']}" alt="{image_name}" />
                <h3>{image_name.replace("_", " ").title()}</h3>
            </a>
"""
            div_counter += 1

    if div_counter % 8 != 0:
        html += '        </div>\n'

    # Close the HTML structure
    html += """
            </section>
        </section>
        <footer id="footer">
            <p>&copy; CompanyNameComingSoon. All rights reserved. Design: <a href="https://templated.co/">TEMPLATED</a></p>
        </footer>
    </div>
    <script src="assets/js1/jquery.min.js"></script>
    <script src="assets/js1/jquery.poptrox.min.js"></script>
    <script src="assets/js1/skel.min.js"></script>
    <script src="assets/js1/main.js"></script>
</body>
</html>
"""
    return html

# Generate the HTML
html_content = generate_html(fulls_folder, thumbs_folder)

# Write the HTML to a file
with open("C:/Users/mahav/OneDrive/Desktop/Portfolio/new.html", 'w') as f:
    f.write(html_content)

print("HTML file generated successfully.")
