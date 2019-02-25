import glob
import os

# file_path = "content/about.html"
# file_name = os.path.basename(file_path)
# print(file_name)
# name_only, extension = os.path.splitext(file_name)
# print(name_only)

#read in all HTML files
content_html_files = glob.glob("content/*.html")
docs_html_files = glob.glob("docs/*.html")
docs_content = content_html_files + docs_html_files
print(docs_content)

# TEMPLATE = template = open("templates/base.html").read()
with open("templates/base.html", "r") as file:
    TEMPLATE = file.read()

PAGES = []

def generate_list():
    content_html_files = glob.glob("content/*.html")
    docs_html_files = glob.glob("docs/*.html")
    docs_content = content_html_files + docs_html_files
    print(docs_content)

def read_content(filename):
    return open(filename).read()


def apply_template(a_string):
    """ read template file and combine with content  """
    return TEMPLATE.replace("{{content}}", a_string)  # string replacing


def write_content(content, output_filename):
    """ loop through pages and write content to output files """
    with open(output_filename, "w+") as outfile:
        outfile.write(content)


def main():
    """ invoke write content function """
    for page in PAGES:
        content = read_content(page["filename"])
        templated_content = apply_template(content)
        write_content(templated_content, page["output"])


if __name__ == "__main__":
    main()
