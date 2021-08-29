
if [[ ! -d "/venv/" ]]
then
    python3 -m venv venv
fi

source venv/bin/activate
pip3 install -r requirements.txt
export FLASK_APP=main
export FLASK_ENV=development
flask run