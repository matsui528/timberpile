import argparse
from dataclasses import dataclass, field
import csv

@dataclass
class Person:
    """
    A class representing a person.

    Attributes:
    -----------
    id : int
        The ID of the person.
    first_en : str
        The first name of the person in English.
    last_en : str
        The last name of the person in English.
    first_jp : str
        The first name of the person in Japanese.
    last_jp : str
        The last name of the person in Japanese.
    web : str
        The website of the person.
    """
    id: int
    first_en: str
    last_en: str
    first_jp: str
    last_jp: str
    web: str

    def __post_init__(self):
        """
        Convert the ID to an integer if it is a string.
        """
        self.id = int(self.id)

    def name(self, lang="en", link=False):
        """
        Get the name of the person.

        Parameters:
        -----------
        lang : str, optional
            The language of the name. Default is "en".
        link : bool, optional
            Whether to include a link to the person's website. Default is False.

        Returns:
        --------
        str
            The name of the person.
        """
        assert lang in ["en", "jp"]
        assert link in [True, False]

        if lang == "en":
            s = f'{self.first_en} {self.last_en}'
        else:
            s = f'{self.last_jp}{self.first_jp}'

        if link and len(self.web) > 0:
            s = f'<a href="{self.web}">{s}</a>'

        return s
    

@dataclass
class Paper:
    """
    A class representing a paper.

    Attributes:
    -----------
    id : int
        The ID of the paper.
    title : str
        The title of the paper.
    booktitle : str
        The booktitle of the paper.
    booktitle_short : str
        The short version of the booktitle of the paper.
    year : int
        The year of the paper.
    pdf : str
        The PDF file of the paper.
    authors : list[Person], optional
        The authors of the paper. Default is an empty list.
    """
    id: int
    title: str
    booktitle: str
    booktitle_short: str
    year: int
    pdf: str
    authors: list[Person] = field(default_factory=list)

    def __post_init__(self):
        """
        Convert the ID to an integer if it is a string.
        """
        self.id = int(self.id)

    def md(self):
        """
        Get the Markdown representation of the paper.

        Returns:
        --------
        str
            The Markdown representation of the paper.
        """
        body = '- '
        for author in self.authors:
            body += f'{author.name()}, '
        body += f'"{self.title}", {self.booktitle_short}, {self.year}.\n'
        return body
    
    def html(self):
        """
        Get the HTML representation of the paper.

        Returns:
        --------
        str
            The HTML representation of the paper.
        """
        body = '\t<li>'
        for author in self.authors:
            body += f'{author.name(lang="jp", link=True)}, '
        body += f'"{self.title}", {self.booktitle_short}, {self.year}.</li>\n'
        return body

    def bibtex(self):
        """
        Get the BibTeX representation of the paper.

        Returns:
        --------
        str
            The BibTeX representation of the paper.
        """
        body = f"@inproceedings{{{self.booktitle_short}_{self.year}_{self.id},\n"
        body += f"\tauthor={{"
        for author in self.authors:
            body += f'{author.name()} and '
        body = body[:-5] + f"}},\n"  # remove the last " and "
        body += f"\ttitle={{{self.title}}},\n"
        body += f"\tbooktitle={{{self.booktitle} ({self.booktitle_short})}},\n"
        body += f"\tyear={{{self.year}}}\n"
        body += f"}}\n\n"
        return body



def main(args):
    """
    The main function of the program.

    Parameters:
    -----------
    args : argparse.Namespace
        The command line arguments.
    """

    # Read the person information.
    with open(args.person, "rt") as f:
        persons = {int(row["id"]): Person(**row) for row in csv.DictReader(f)}

    # Read the paper information.
    with open(args.paper, "rt") as f:
        papers = [Paper(**row) for row in csv.DictReader(f)]

    # Read the paper-author information.
    with open(args.paper_author, "rt") as f:
        for row in csv.DictReader(f):
            paper_id = int(row["paper_id"])
            person_id = int(row["person_id"])
            assert paper_id < len(papers) and person_id in persons

            # Add the author to the paper.
            papers[paper_id].authors.append(persons[person_id])
    
    # Render the output.
    body = ""
    if args.output_type == "md":
        for paper in papers:
            body += paper.md()
    elif args.output_type == "html":
        body += f'<ul>\n'
        for paper in papers:
            body += paper.html()
        body += f'</ul>\n'
    elif args.output_type == "bibtex":
        for paper in papers:
            body += paper.bibtex()

    # Write the output.
    with open(args.output, "wt") as f:
        f.write(body)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--person", type=str, default="src/person.csv",
                        help="The path to the CSV file containing information about people.")
    parser.add_argument("--paper", type=str, default="src/paper.csv",
                        help="The path to the CSV file containing information about papers.")
    parser.add_argument("--paper_author", type=str, default="src/paper_author.csv",
                        help="The path to the CSV file containing information about paper authors.")
    parser.add_argument("--output", type=str, default="output.md",
                        help="The path to the output file.")
    parser.add_argument("--output_type", type=str, choices=["md", "html", "bibtex"],
                        default="md",
                        help="The type of output to generate. Can be 'md', 'html', or 'bibtex'.")

    args = parser.parse_args()
    main(args)