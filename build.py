
# TEMPLATE = template = open("templates/base.html").read()
with open("templates/base.html", "r") as file:
    TEMPLATE = file.read()

PAGES = [
    {
        "filename": "content/index.html",
        "output": "docs/index.html",
        "title": "Home",
    },
    {
        "filename": "content/about.html",
        "output": "docs/about.html",
        "title": "About Me",
    },
    {
        "filename": "content/contact.html",
        "output": "docs/contact.html",
        "title": "Contact",
    },
    {
        "filename": "content/music.html",
        "output": "docs/music.html",
        "title": "Music",
    },
    {
        "filename": "content/photography.html",
        "output": "docs/photography.html",
        "title": "Photography",
    },
    {
        "filename": "content/projects.html",
        "output": "docs/projects.html",
        "title": "Projects",
    },
]

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
