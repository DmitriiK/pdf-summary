# Sprint 1
## Uploading of PDF files and processing
### Front-End
Web page to upload file:
- Select a file from the local machine and upload it
- Show the status of uploading
- Use  bottom part of the same page to display the list of uploaded files
### Back-End
- Persist the results of that process with attributes: file_name, upload_date, summary using SQLLight

## use bottom part of the  page to display the results
The upper part of that page is a list of files with file names and upload dates.


# Sprint 2 - Asycronous processing
# #Upload procedure
- Should not insert data into SQL - it should add message with file pathes to Azure Queue
## Processing module - separate module for processing of the queue that:
- takes message from the queue, takes file path and feed this files to Gemini for summarization
- after that it inserts (or update if file with such name existgs) records in SQl,  



# Non-functional requirements
- Use only HTML, CSS, and JavaScript for the front-end
- Use Python, for example, FastAPI for the back-end
- Use SQLLight as persistence layer
- Use Azure Queue for asyncronous processing
- your solution should be simple
- Use uv as package manager and .toml files for dependencies
- Use storage acount connection string for access to the queue
- storage account connection string and Gemini token should be in .env file
- path to SQL DB, upload directory path should be specified in separate configuration py file

