# COVID19-Trondelag

This is a simple python script which gets information covering the spread of COVID-19 in Trøndelag fylkeskommune in Norway from the API delivered by Addressa.no
While browsing their webpage I saw a table which was recently updated and found that the same table was being used in multiple articles.
The table is updated on a regular basis and is accessed by a simple web API, thanks to Addresseavisa for delivering this service.


```bash
	sudo apt-get install python3-tk
	~/../COVID_TRD$ pipenv shell
	~/../COVID_TRD$ pip install -r requirements.txt
	~/../COVID_TRD$ python app/main.py
```


Fra SSH terminal:
```bash
	export DISPLAY=:0
	*Kjør script*
	ctrl+z
	bg
	disown
```
