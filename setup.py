import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME="nlpPro"
Author_User_Name="3101ajeet"
Src_Repo="textSummarizer"
Author_Email="ajitsingh.hr01@gmail.com"

setuptools.setup(
    name=Src_Repo,
    version=__version__,
    author=Author_User_Name,
    author_email=Author_Email,
    description="Text Summarizer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{Author_User_Name}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{Author_User_Name}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)