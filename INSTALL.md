# Hunter Codefest 2020-2021

# How to install

1. clone the repo 
    ```
    $ git clone git@github.com:huntercodefest/winter-2021-codefest-submissions-greenturtle.git 
    ```

2. cd into folder 

    ```
    $ cd winter-2021-codefest-submissions-greenturtle
    ```

3. activate virtual environment
    ```
    $ . path/to/venv/bin/activate

    (venv) $ pip install --upgrade pip
    ```

4. install dependencies with the requirements.txt 
   ```
   (venv) $ pip install -r requirements.txt
   ```
5. get api keys 

# How to run 

## Server 

1. Start the server 

    ```
   (venv) $ python app.py
    ```

## Firefox Extension 

1. Go to about:debugging page on Firefox

2. Click on "This Firefox" and then click on "Load Temporary Add-on..."

3. You will be prompted to choose a file. In the description folder of the cloned repository select description.js

4. The extension is now installed until you restart Firefox


## Chrome Extension 
1. Go to chrome://extensions/

2. Click on "Load unpacked"

3. You will be prompted to choose a file / folder. Select the folder `description`

4. The extension is now installed 
