## Welcome

This is the assignment application.
Container 4 apis.
1. Get the data for a given key
2. Set a given key-pair value
3. Search values/keys based on query.

<hr>



Project Structure
--------

  ```sh


  ├── README.md
  ├── app.py
  ├── config.py
  ├── error.log
  ├── requirements.txt
  ├── data.json
  |__tests.py
  |__ utils
    |__utilities.py
  ```

### Test case coverage 
```
(.testenv) anushka@Anushkas-MacBook-Air application % coverage run tests.py 
[2022-04-01 06:06:32,484] INFO in app: Key data has value ['kartikeyan', 'value']
[2022-04-01 06:06:32,486] WARNING in app: Key key_do_not_exists is not available in our database
......
----------------------------------------------------------------------
Ran 6 tests in 0.015s

OK
```

### Coverage Report

```
Name                 Stmts   Miss  Cover
----------------------------------------
app.py                  73     34    53%
config.py                8      0   100%
tests.py                40      0   100%
utils/utilities.py      20      4    80%
----------------------------------------
TOTAL                  141     38    73%
```



### Quick Start

1. Clone the repo
  ```
  $ git clone git@github.com:kartikeyangupta/lummo-assignment.git
  $ cd lummo-assignment
  ```

2. Initialize and activate a virtualenv:
  ```
  $ python3 -m venv .testenv
  $ source .testenv/bin/activate
  ```

3. Install the dependencies:
  ```
  $ pip install -r requirements.txt
  ```

5. Run the development server:
  ```
  $ python app.py
  ```

6. Navigate to [http://localhost:6000](http://localhost:6000)
7. Navigate to [http://perconnected.com:6000](http://perconnected.com:6000)


8. Use docker-compose to make the service run
```
$ cd to_directory
$ docker-compose up -d
```