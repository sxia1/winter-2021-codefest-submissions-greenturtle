# Hunter Codefest 2020-2021

# How to install

1. Clone the repo 
    ```
    $ git clone git@github.com:huntercodefest/winter-2021-codefest-submissions-greenturtle.git 
    ```

2. `cd` into folder 

    ```
    $ cd winter-2021-codefest-submissions-greenturtle
    ```

3. Activate your virtual environment and upgrade `pip`
    ```
    $ . path/to/venv/bin/activate

    (venv) $ pip install --upgrade pip
    ```

4. Install the dependencies with the requirements.txt 
   ```
   (venv) $ pip install -r requirements.txt
   ```
5. Register for an API key  
    We use the [OCR.SPACE Free OCR API](http://ocr.space/OCRAPI). [Register here](http://eepurl.com/bOLOcf).  
    <sub>If that link doesn't work, go [here](http://ocr.space/OCRAPI) (http://ocr.space/OCRAPI) and check for the sign up link in the API Plan chart under "Free"</sub>



# How to run 

## Server 

We have it hosted on [Heroku](https://greenturtle.herokuapp.com/) (https://greenturtle.herokuapp.com/) and the extension uses it :) 

## Firefox Extension 

1. Go to about:debugging page on Firefox

2. Click on "This Firefox" and then click on "Load Temporary Add-on..."

3. You will be prompted to choose a file. In the description folder of the cloned repository select description.js

4. The extension is now installed until you restart Firefox


## Chrome Extension 

1. Go to chrome://extensions/

2. Exnsure that "Developer mode" is on by checking the toggle in the top right-hand corner  
    <sub>This allows you to load "unpacked directories" as if though they were packaged extensions</sub>

3. Click on "Load unpacked" to load an extension 

3. You will be prompted to choose a file / folder. Select the folder `description`

4. The extension is now installed 
