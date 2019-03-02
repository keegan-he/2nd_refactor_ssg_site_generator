import glob
import os
from jinja2 import Template

def build_pages():
    """read in all HTML files"""
    content_html_files = glob.glob("content/*.html")
    #print(content_html_files)

    PAGES = []

    for file_path in content_html_files:
        file_name = os.path.basename(file_path)
        name_only, extension = os.path.splitext(file_name)

        PAGES.append({
            "filename": file_path,
            "title": name_only.title(),
            "output": file_name,
        })

    #print(PAGES)
    return PAGES

def read_content(filename):
    '''read content in'''
    return open(filename).read()

def apply_template(filename, title, pages):
    """ read template file and combine with content  """
    index_html = open(filename).read()
    template_html = open("templates/base.html").read()
    template = Template(template_html)
    return template.render(
        pages=pages,
        title=title,
        content=index_html,
    )

def write_content(content, output_filename):
    """ loop through pages and write content to output files """
    with open("docs/{}".format(output_filename), "w") as outfile:
        outfile.write(content)

def main():
    """ invoke write content function """
    pages = build_pages()
    for page in pages:
        templated_content = apply_template(page["filename"], page["title"], pages)
        write_content(templated_content, page["output"])

if __name__ == "__main__":
    main()
