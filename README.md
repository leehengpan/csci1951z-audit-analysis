## CSCI 1951Z EEOC Audit Final Project

In this project, we play the role of an auditing team placed by EEOC to investigate Bold Bank's hiring practices. Bold Bank is a financial institution that has recently implemented a new hiring system developed by Providence Analytica to streamline its recruitment process. The purpose of this audit is to investigate complaints that allege discriminatory outcomes in the new hiring process. Through our analysis, we hope to ascertain that the candidate selection process is not plagued by discriminatory outcomes because of a person's race, color, religion, sex, national origin, age, and disability.

To conduct our review, we will rely on a combination of stakeholder interviews-- job applicant, Providence Analytica, and Bold Bank representatives-- and automated flows to probe the resume scorer and candidate evaluator models. At a high level, the hiring system consists of two phases: 
	1. A resume scoring model that assigns a score of 0 to 10 to a CSV-formatted resume, indicating the candidate's suitability for a specific role
    2. A candidate evaluator model customized to the company's preferences, utilizes the resume scores to generate a binary outcome for whether the candidate should receive an interview.


----- xxxxx ------


Here's a brief overview of the structure of this repo:

`report.pdf`- a compilation of the different tasks of the auditing process-- introducing the project's scope, methodology, detailed observations, results, and recommendations.

`audit-analysis.ipynb`- is the primary notebook to refer to understand our auditing methodology, observations, and results with complete detail.

`dataprep-flow.ipynb`- is a series of short code snippets organized to make the process of creating the synthetic dataset. Run this file only if you wish to refresh the dataset we have created. Note that, this may cause some discrepancies from the values we report.

`src/`- contains short scripts that we wrote to simplify the creation of a synthetic dataset

`data/`- contains the synthetic dataset created in the notebook `dataprep-flow.ipynb`.

`plots/`- contains all plots we have created through our analysis as in the notebook `audit-analysis.ipynb`.

`environment.yml`- A yml file of the conda environment configuration used in this project.


----- xxxxx ------

Make sure to refer to `environment.yml` file to resolve any dependency issues.