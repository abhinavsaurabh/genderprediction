# gender-detect

![Gender Detect Demo](https://i.imgur.com/6CVLRpW.png)

Infer the gender based on the first name of a person.

### Backstory
Developed during one day codecamp organized by Yomari at [LOCUS 2016](https://www.facebook.com/events/142445032843455).

### Built With

* [Python](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)

### Local Development
To install these interactives on your local machine:
* Clone this repository to your local machine.
* In the directory where you placed the cloned repo, create a virtual environment for Python and project dependencies in a directory called "venv":
```shell
pip install virtualenv 
virtualenv venv
```
* Activate your virtual environment
```shell
source venv/bin/activate
```
* Install Flask and all required packages:
```shell
pip install -r requirements.txt
```

* Fire up your local webserver:
```shell
python app.py
```

* In a web browser, go to [localhost:5000](http://localhost:5000/), and you should see the development site! Please not that the terminal window you are running the development site in must stay open while you are using the site.

* When development is complete, terminate the local web server by typing ```CONTROL + C```. Also deactivate the virtual environment:
```shell
deactivate
```

#### Authors
- [Amit Chaudhary](http://amitness.com)
- [Kiran Koirala](http://twitter.com/koiralakiran01)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
