First, make sure you have Python and tsc installed.

tsc is only needed for development using Typescript, if you just need to run the app, no need to have it.

In order to use Typescript and auto-compile into javascript, run the following commands from the root folder:

```
cd static
tsc -w
```

Run the following commands from the root folder to start the app: 

```
python -m pip install -r requirements.txt
export FLASK_ENV=development
python -m flask run
```
(on Windows use `set` instead of `export`)

You must have the 2 terminals open and running. One runs the app and the other compiles your Typescript. 
