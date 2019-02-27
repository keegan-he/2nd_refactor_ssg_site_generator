import glob
import os
from jinja2 import Template

def build_pages():
        
    """read in all HTML files"""
    content_html_files = glob.glob("content/*.html")
    print(content_html_files)

    PAGES = []

    for file_path in content_html_files:
        file_name = os.path.basename(file_path)
        print(file_name)
        name_only, extension = os.path.splitext(file_name)
        print(name_only)


        PAGES.append({
            "filename": file_path,
            "title": file_name,
            "output": "docs/{}".format(file_name),
        })

    print(PAGES)
    return PAGES


def read_content(filename):
    return open(filename).read()


def apply_template(filename, title):
    """ read template file and combine with content  """
    index_html = open(filename).read()
    template_html = open("templates/base.html").read()
    template = Template(template_html)
    return template.render(
        title=title,
        content=index_html,
    )

def write_content(content, output_filename):
    """ loop through pages and write content to output files """
    with open(output_filename, "w") as outfile:
        outfile.write(content)


def main():
    """ invoke write content function """
    for page in build_pages():
        templated_content = apply_template(page["filename"], page["title"])
        write_content(templated_content, page["output"])


if __name__ == "__main__":
    main()
