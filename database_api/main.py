from dotenv import load_dotenv

load_dotenv() # Loads environemt variables automatically when app runs instead of needing to be declared each time

from app import app 

if __name__ == '__main__': # only runs if the file is run directly not when it is imported, starts the web server
    app.run(debug=True) # enables debug mode only for development not for use in production