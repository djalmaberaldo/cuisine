
echo 'Setting up the environment'


echo 'Backend first...'
chmod 777 -R .
cd backend

if [[ ! -d "venv" ]]
then
    echo 'Creating venv..'
    python3 -m venv venv

    echo 'Activating venv...'
    source venv/bin/activate
    
    echo 'Installing requirements.txt'
    pip3 install -r requirements.txt
fi

echo 'Activating venv...'

source venv/bin/activate
export FLASK_APP=main
export FLASK_ENV=development
flask run
