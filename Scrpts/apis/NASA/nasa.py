from build_web import build_web_page , Template

html_template = Template('''<!DOCTYPE html>
                            <html>
                            <head>
                            <title>25 Curiosity photos</title>
                            </head>
                            <body>

                            <h1>25 Curiosity photos</h1>   

                            $body

                            </body>
                            </html>
                        ''')

build_web_page(html_template)