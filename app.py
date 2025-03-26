from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Getting Started with AWS for Developers</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
            }
            header {
                background-color: #0073e6;
                color: white;
                text-align: center;
                padding: 20px;
            }
            header h1 {
                margin: 0;
                font-size: 2.5em;
            }
            main {
                padding: 20px;
                text-align: center;
                background-color: white;
                border-radius: 10px;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                margin-top: 20px;
            }
            h2 {
                color: #333;
            }
            p {
                font-size: 1.1em;
                color: #555;
            }
            .cta {
                background-color: #28a745;
                color: white;
                padding: 10px 20px;
                text-decoration: none;
                border-radius: 5px;
                font-size: 1.2em;
                margin-top: 20px;
                display: inline-block;
            }
            .cta:hover {
                background-color: #218838;
            }
            .link-list {
                list-style-type: none;
                padding: 0;
            }
            .link-list li {
                margin: 10px 0;
            }
            footer {
                text-align: center;
                padding: 10px;
                background-color: #222;
                color: white;
                position: fixed;
                bottom: 0;
                width: 100%;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Welcome to AWS Developer Training</h1>
            <p>Learn how to deploy applications with EC2, Lambda, and RDS</p>
        </header>

        <main>
            <h2>Course Details</h2>
            <p><strong>Date:</strong> March 26th</p>
            <p><strong>Time:</strong> 11:30 AM – 01:00 PM</p>
            <p><strong>Topic:</strong> Getting Started with AWS for Developers: Deploying Applications with EC2, Lambda, and RDS</p>

            <h2>Join the Webinar</h2>
            <ul class="link-list">
                <li><a href="https://zoom.us/webinar/register/7317411552853/WN_zVywNSChQJeXfxYmpb8QUg" class="cta" target="_blank">Register Now</a></li>
                <li><a href="https://www.youtube.com/watch?v=N50HDBRjrAE" class="cta" target="_blank">Watch Live on YouTube</a></li>
                <li><a href="https://www.linkedin.com/events/7309835931727892480/comments/" class="cta" target="_blank">Join the LinkedIn Event</a></li>
            </ul>
        </main>

        <footer>
            <p>&copy; 2025 AWS Developer Training | All rights reserved</p>
        </footer>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
