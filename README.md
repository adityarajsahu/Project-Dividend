<!-- PROJECT LOGO AND NAME -->
<div align="center">
    <h1 align="center"><strong>PROJECT DIVIDEND</strong></h3>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
        <li><a href="#demonstration">Demonstration</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#create-virtual-environment">Create virtual environment</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#user-interface">User Interface</a></li>
    <li><a href="#contributors">Contributors</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

We have developed a web application that takes extracts important stock data such as latest news related to National Stock Exchange, American Depository Receipt, Global Depository Receipt, Market Turnover, Option Flows and Top Surfers in the market. This will help the user in better understanding the current status of the stock market.

### Built With

* [![Python][python-image]][python-url]
* [![Django][Django-image]][Django-url]
* [![Beautiful Soup][bs-image]][bs-url]
* [![nsepython][nsepython-image]][nsepython-url]
* [![anaconda][Anaconda-image]][Anaconda-url]

### Demonstration

https://user-images.githubusercontent.com/54609034/210134621-5d73e063-4457-4aad-bb30-9f027be683b8.mp4



<!-- PREREQUISITES AND INSTALLATIONS -->
## Getting Started
To test the web application, you need to create a virtual environment and install the dependencies.

### Prerequisites 
To test the web application, follow the instructions below and install the prerequisites.

* Install Anaconda Distribution <br>

* Open Anaconda Prompt and Update conda environment
```
conda update conda
```

### Create Virtual Environment
Set up a virtual environment
```
conda create -n venv python=3.8
conda activate venv
```
### Installation

Install dependencies in the virtual environment
```
pip install -r requirements.txt
``` 

Migrate Database and Run Server

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```  

## User Interface

![ui1](https://user-images.githubusercontent.com/54609034/210134695-ff23c1f0-6d4d-4315-8671-0332ed9df5a8.png)
![ui2](https://user-images.githubusercontent.com/54609034/210134699-2600436c-823d-496b-af6d-e7b5dbea52ef.png)
![ui3](https://user-images.githubusercontent.com/54609034/210134713-5ae43efa-8519-45e1-81c9-d8e3e6be68ee.png)
![ui4](https://user-images.githubusercontent.com/54609034/210134714-061adfff-4411-4a62-a105-ada68e719bd7.png)


## Contributors
<table>
  <tr>
    <td align="center">
        <a href="https://github.com/adityarajsahu">
            <img src="https://avatars.githubusercontent.com/u/54609034?v=4" width="100px;" alt=""/>
            <br />
            <sub><b>Adityaraj Sahu</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/prats778">
            <img src="https://avatars3.githubusercontent.com/u/58729042?v=4" width="100px;" alt=""/>
            <br />
            <sub><b>prats778</b></sub>
        </a>
    </td>
  </tr>
</table>



<!-- MARKDOWN LINKS & IMAGES -->
[Django-image]: https://img.shields.io/badge/django-000000?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://www.djangoproject.com/
[python-image]: https://img.shields.io/badge/python-20232A?style=for-the-badge&logo=python&logoColor=61DAFB
[python-url]: https://www.python.org/
[bs-image]: https://img.shields.io/badge/BeautifulSoup-35495E?style=for-the-badge&logo=BeautifulSoup&logoColor=4FC08D
[bs-url]: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
[nsepython-image]: https://img.shields.io/badge/nsepython-4A4A55?style=for-the-badge&logo=nsepython&logoColor=white
[nsepython-url]: https://aeron7.github.io/nsepython/
[Anaconda-image]: https://img.shields.io/badge/Anaconda-563D7C?style=for-the-badge&logo=anaconda&logoColor=white
[Anaconda-url]: https://repo.anaconda.com/archive/Anaconda3-2022.05-Windows-x86_64.exe
