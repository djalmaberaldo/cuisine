cd frontend/cuisine-app
if [[ ! -d "node_modules" ]]
then
    npm install
fi
ng serve
