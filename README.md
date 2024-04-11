# WIS Python programming course started on 2024.04

[course](https://erez.weizmann.ac.il/apx/f?p=186:30:::NO::pid,pprev:14800,14473)

## Students

| Home page | Repo | Assignments | Project | Status |
| --------- | ---- | ----------- | ------- | ------ |
| [Meir Sylman](https://meirsylman.github.io/)       | [repo](https://github.com/MeirSylman/MeirSylman.github.io)   |  | | |
| [Omer Sapir](https://omersapir.github.io/)         | [repo](https://github.com/OmerSapir/OmerSapir.github.io)     |  | | |
| [Omer Zachar](https://omerzachar.github.io/)       | [repo](https://github.com/OmerZachar/omerzachar.github.io)   |  | | |
| [Shahar Garin](https://shahargarin.github.io/)     | [repo](https://github.com/ShaharGarin/shahargarin.github.io) |  | | |


## Plan

### Schedule

* 2024.04.11 9:00-12:00
* 2024.04.18 9:00-12:00
* 2024.04.25 Pesach
* 2024.05.02 9:00-12:00
* 2024.05.09 9:00-12:00
* 2024.05.16 9:00-12:00
* 2024.05.23 9:00-12:00
* 2024.05.30 9:00-12:00
* 2024.06.06 9:00-12:00
* 2024.06.13 9:00-12:00
* 2024.06.20 9:00-12:00

### Participation in the lectures

There is no requirement to participate in the lectures. You will be able to watch the videos later. However, it is recommended to participate as that gives you an opportunity to ask questions.

### Timestamps

Each video will be around 1 hour long. In order to make it easier to access the specific topics I would like to add timestamps to each video. A timestamp looks like this:

```
00:00 Start
01:30 Installation
```

Meaning at 1 minute 30 seconds I started to talk about Installation.

I'll need volunteers to prepare these timestamps for each video on the day after the lecture.
You basically need to watch the video and write down all the points where you think you or someone else would like to jump to. You can see such timestamps in the comments of many YouTube videos.
We will have an [issue](https://github.com/szabgab/wis-python-course-2024-04/issues) where you'll be able to volunteer.

### Assignments

There will be assignments after every lecture. You will submit them via GitHub. I'll explain the details during the lectures.

### Project

Towards the end of the course you'll be asked to do a project.
First you need to submit a proposal for the project and when it is accepted then implement it.
The project should be something that is useful for your studies or at least it is fun for you to make.
Ask in the lab where you work what needs are there that you might implement as your final project.
You can get inspiration from the projects [listed here](https://code-maven.com/programming-bootcamp-for-scientists)
and the [projects of the 2023 autumn semester](https://github.com/szabgab/wis-python-bootcamp-2023-12).

### Grades

* Each assignment counts as 5% (we will have 10 of them).
* The project proposal is 15%.
* The project is 35%.

* The project is a requirement. Witthout that you won't get a passing grade.

### Slides

During the course I'll use some of the [slides that can be found here](https://code-maven.com/slides/python/).
These slides are publicly available and will remain on the web site after the course is over.

### Videos in English

There are [recording of this course from 3 years ago](https://code-maven.com/programming-bootcamp-for-scientists).

There are also [recordings from the 2023 autumn semester](https://github.com/szabgab/wis-python-bootcamp-2023-12).

My [English-language YouTube channel](https://code-maven.com/youtube).

You can watch those, but be also warned, this semester the order of the material will be different.

### Videos in Hebrew

Some of the material is also available in Hebrew. You can find them [on my website](https://he.code-maven.com/)
and in my [Hebrew-language YouTube channel](https://he.code-maven.com/youtube).


### Language

The standard language of WIS and of this course is English.

However, when on one-on-one conversions I'd be happy to speak in Hebrew, Hungarian, Spanish, or Ladino.

### Installations

There is no need to install anything up front. We'll do that during the class.


## Day 1

## Videos

* [Day 1 part 1](https://youtu.be/xjnTAHI_Vvg)
* [Day 1 part 2](https://youtu.be/xFOlDv6o-NQ)
* [Day 1 part 3](https://youtu.be/lqUQit7PtDM)


* Overview:
    * git, GitHub a VCS
    * [Python](https://www.python.org/) - the [source code of Python](https://github.com/python/cpython)
    * [PyPI](https://pypi.org/)

* [Duck Duck Go](https://duckduckgo.com/) search engine.

* GitHub:
    * [BioPython](https://biopython.org/) - [source code](https://github.com/biopython/biopython) - [the source of their web site](https://github.com/biopython/biopython.github.io) - the [pull request fixing typo](https://github.com/biopython/biopython.github.io/pulls?q=is%3Apr+author%3Aszabgab)
    * Other projects hosted on GitHub.
    * GitHub Issues.
    * GitHub Pages

* The [cm-demo GitHub user]()
    * [Repository of GitHub pages](https://github.com/cm-demo/cm-demo.github.io/) (it will be renamed later)
    * [The web site](https://cm-demo.github.io/)

* [Static Site Generators](https://jamstack.org/generators/)
    * GitHub Pages default to use [Jekyll](https://jekyllrb.com/) but you could switch to something else.

* Install [gis-scm](https://git-scm.com/)
    * Don't forget to set the default editor to Notepad or some other simple one. Don't keep vim.
* Instal [VS Code](https://code.visualstudio.com/)
* Create GitHub Pages
* Markdown and [GitHub Flavored Markdown](https://github.github.com/gfm/)
* Command line Git.
* Configure git client

```
git config --global user.email your@mail.address.com
git config --global user.name "Your Name"
```

Git commands:

```
git clone ...
git status
git add
git commit -m "some explanation"
git push
```

* Generate ssh private key and add it to your GitHub Account.

```
ssh-keygen                 (just press ENTER several times accepting all the defaults)
cat ~/.ssh/....pub
```

* (git) bash commands

```
pwd               print working directory
cd  /c/Users      change directory
```

In the File Explorer click on "view" and then mark the check-boxes: "File name extensions" and "Hidden items"

### Assignment (day 1)

* Create your own GitHub
* Create you own web site on GitHub pages
* Open an issue on our shared GitHub project with the link to that site and to the repository.

* Dead-line 2024.04.15 24:00

