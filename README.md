# Running api locally

#### Create config.json file
1. `cp config.json.template config.json`
2. Fill out credentials of db in specified fields.

#### For development
1. `pip3 install virtualenv` 
2. `virtualenv working_env`
3. `source working_env/bin/activate`

#### Running API
1. `pip3 install -r requirements.txt`
2. `python3 spin_bike_api.py`