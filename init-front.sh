cd frontend/cuisine-app
chmod 777 -R .
if [[ ! -d "node_modules" ]]
then
    npm install
fi
ng serve
