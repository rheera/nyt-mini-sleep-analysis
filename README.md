<p align="center">
    <img src="https://mwcm.nyt.com/dam/mkt_assets/img/games/mini.png?raw=true" alt="NYT Mini Crossword Logo" width="190" height="100"/>
</p>

# New York Times Mini Crossword Analysis

This is a side project I'm doing to explore trends in crossword completion for the Mini Crossword offered by the [`New York Times (NYT)`](https://www.nytimes.com/crosswords/game/mini).

### Task 1: Data Collection

Collecting the data was a little tricky since I could only view past scores on the official NYT Games app. I first expanded on [`@alexchandy13`](https://github.com/alexchandy13/nyt-mini-stats/tree/main)'s code. I automated tapping through each day on my iPhone and screen recording it. Then I planned to use OCR, read the data for each frame, and write that to a file. Unfortunately, some of the text wasn't coming out perfectly and I felt I couldn't completely trust the data.

I've now figured out a way to access the data through the API, making it much more trustworthy. Since NYT made it so difficult to collect I don't think they want people to scrape their statistics so I will not upload that part of the code.

## Table of Contents

- [Data Description](#data-description)
- [Files Description](#files-description)
- [Tools](#tools)
- [Deliverables](#deliverables)
  - [Task 1: Data Collection](#task-1-data-collection)
  - [Task 2: Data Wrangling](#task-2-data-wrangling)
  - [Task 3: Exploratory Data Analysis](#task-3-exploratory-data-analysis)
  - [Task 4: Data Visualization](#task-4-data-visualization)
  - [Task 5: Dashboard Creation](#task-5-dashboard-creation)
  - [Task 6: Presentation of Findings](#task-6-presentation-of-findings)
- [Stretch Goals](#stretch-goals)

## Data Description

New York Times (NYT), a daily newspaper company with perhaps the most renown crossword, creates a daily mini crossword where friends can compete. I've compilied a dataset of all mine and my friends scores from January 1, 2022 till April 30, 2024.

The dataset will be available as a .csv file here.

The below table lists the columns in the data.

<details>
 <summary><strong>View Table</strong></summary>
<table>
  <thead>
    <tr>
      <th>Column Name</th>
      <th>Column Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>rank</td>
      <td>
        What place the user finished for the day. (Eg. 1 being first, 2 meaning 2nd etc.)
      </td>
    </tr>
    <tr>
      <td>name</td>
      <td>
        The user's username.
      </td>
    </tr>
    <tr>
      <td>userID</td>
      <td>The user's ID.</td>
    </tr>
    <tr>
      <td>score</td>
      <td>The user's score in seconds. The time the user took to complete the day's puzzle, in seconds.</td>
    </tr>
    <tr>
      <td>date</td>
      <td>The date of the puzzle.</td>
    </tr>
  </tbody>
</table>

</details>

## Data Description

The below table lists the files in this repo and their descrpitions.

<details>
 <summary><strong>View Table</strong></summary>
<table>
  <thead>
    <tr>
      <th>File Name</th>
      <th>File Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>output.tsv</td>
      <td>
        The original dataset I managed to scrape from a screen recording of all the mini scores using OCR. It's not too great.
      </td>
    </tr>
    <tr>
      <td>output.csv</td>
      <td>
        The actual complete dataset collected via the API.
      </td>
    </tr>
    <tr>
      <td>mini_stats_auto.mp4</td>
      <td>The screen recording of all the scores.</td>
    </tr>
    <tr>
      <td>initial_scrape.py</td>
      <td>The functions for scraping the screen recording and writing the data.</td>
    </tr>
  </tbody>
</table>

</details>

## Tools

- [`python`](https://www.python.org/downloads/) v3.12.2
- [`pandas`](https://pandas.pydata.org/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMML0187ENSkillsNetwork31430127-2021-01-01) for managing the data.
- [`numpy`](https://numpy.org/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMML0187ENSkillsNetwork31430127-2021-01-01) for mathematical operations.

## Deliverables

### Task 1: Data Collection

- [ ] Scrape NYT mini data

### Task 2: Data Wrangling

- [ ] Finding Missing Values
- [ ] Determine Missing Values
- [ ] Finding Duplicates
- [ ] Removing Duplicates
- [ ] Normalizing Data

### Task 3: Exploratory Data Analysis

- [ ] Distribution
- [ ] Outliers
- [ ] Correlation

### Task 4: Data Visualization

- [ ] Visualizing Distribution of Data
- [ ] Relationship
- [ ] Composition
- [ ] Comparison

### Task 5: Dashboard Creation

- [ ] Dashboards

### Task 6: Presentation of Findings

- [ ] Final Presentation

## Stretch Goals

- [ ] Add sleep data to capture more insights.

## Considerations & Caveats

Since the NYT mini crossword comes out at 10 pm ET there is a chance users completed the next day's puzzle the day before (eg. The April 30th puzzle comes out at 10 pm on April 29th). The NYT's API I used to capture the data didn't have a way for me to gather when a user completed the puzzle. Also, users with an NYT subscription can complete a past puzzle whenever they want so again they could complete a puzzle sometime in the future. Fortunately (or unfortunately 🤔) most of my friends can't afford the subscription.
