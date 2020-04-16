# The civic repo
This repo contains automation and scripts for testing the Google Civic Information API. 

Using the simple framework provided here, automated tests are launched at the site from a docker container.
Once the tests have completed the container is killed off.  Use the following command to build the container.
```
docker build -t test_robot .
```
The following command launches the test_runner API. The stdout messages in the terminal show test progess and results.
```
docker run test_robot
```
Always remove the last "test_robot" image before building a new image.
```
docker rmi test_robot:latest
```
### /civic_api/tests
Location of tests and test files.

### /civic_api/utilities
Location of support utilites. (not currently used)

### run_tests.sh
The run_tests.sh script is used to copy env files, tests, etc. (if needed), and to execute the tests.

### /reports
Location reports created by the automation or scripts. (not currently used)

## Tests and descriptions
Start here and describe the tests and what they do.
### Test description
