import converter
import os

markdown_path1 = '../in/1.md'
markdown_path2 = '../in/2.md'

html_path = '../out/resultado.html'

def printer(html_text):
    html = open(html_path, 'w')
    html.write(html_text)

def reader():
    markdown = open(markdown_path2, 'r')
    return markdown.read()

def main():
    markdown_text = reader()

    html_text = converter.converter(markdown_text)

    printer(html_text)


if __name__ == "__main__":
    main()