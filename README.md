# weather_api
##Provides REST API for temperature and pressure data from noaa.gov

API allows for temperature and pressure data to be accessed from files at the following NOAA.gov location:
`https://tgftp.nws.noaa.gov/data/observations/metar/decoded/`

Each filename is a location key, so in order to pull temperature data from the KBOS.TXT file use the following format:
`http://127.0.0.1:5000/temperature?key=KBOS`

Whereas the pressure data can be accessed using:
`http://127.0.0.1:5000/pressure?key=KBOS`

Invalid location keys will return a 404 message, while valid location keys that do not contain the requested data will inform the user the data could not be found
