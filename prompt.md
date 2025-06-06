# Features
## Uploading of PDF files and processing
### Front-End
Web page to upload file:
- Select a file from the local machine and upload it
- Show the status of uploading

### Back-End
- Send these files to Gemini using an API for summarization
- Persist the results of that process with attributes: file_name, upload_date, summary

## Web page to display the results
The upper part of that page is a list of files with file names and upload dates.
The bottom part is the summary for the file that has been selected in the grid in the upper part.

# Non-functional requirements
- Use only HTML, CSS, and JavaScript for the front-end
- Use Python, for example, FastAPI for the back-end
- The processing of PDF files is supposed to be done asynchronously, using azure queues
- Use SQLLight to persist processed data - file names, summary, date of upload
- We are using uv as packet manager

# Assumptions
- File names are unique. If the file is already uploaded we should update data in persistence layer

# Deployment
- All this supposed to be launched on Azure VM. Write as separate .md file some manual for deployment


