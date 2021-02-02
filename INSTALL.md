# Hunter Codefest 2020-2021

# How to install

1. Clone the repo 
    ```
    $ git clone git@github.com:huntercodefest/winter-2021-codefest-submissions-greenturtle.git 
    ```

2. `cd` into the folder 

    ```
    $ cd winter-2021-codefest-submissions-greenturtle
    ```

# How to run 

## Server 

We have it hosted on [Heroku](https://greenturtle.herokuapp.com/) (https://greenturtle.herokuapp.com/) and the extension uses it :) 

The code for it is under [greenturtle](https://github.com/rachel-ng/greenturtle) if you're curious. 

It's also included as a submodule (under `/server`) in this repo

## Extension 

### API key  

#### Register For an API Key 

We use the [OCR.SPACE Free OCR API](http://ocr.space/OCRAPI). 

1. [Register here](http://eepurl.com/bOLOcf).  
    <sub>If that link doesn't work, go [here](http://ocr.space/OCRAPI) (http://ocr.space/OCRAPI) and check for the sign up link in the API Plan chart under "Free"</sub>

2. You will be sent an email with a link to confirm your subscription, click the link.  
    <sub>The mailing list supposedly just sends out API related announcements</sub> 

3. Your API key will be emailed to you :)  
    Please keep it handy for the next step!

#### Use the API Key 

1. Open `description/description.js` with any text editor 

2. Replace the placeholder `var KEY`, with the API key you received
    ```js
    var KEY =  "your_api_key";
    ```

3. You can move on to installing the extension now!

### Firefox Extension 

1. Go to about:debugging page on Firefox

2. Click on "This Firefox" and then click on "Load Temporary Add-on..."

3. You will be prompted to choose a file. In the description folder of the cloned repository select description.js

4. The extension is now installed until you restart Firefox


### Chrome Extension 

1. Go to chrome://extensions/

2. Ensure that "Developer mode" is on by checking the toggle in the top right-hand corner  
    <sub>This allows you to load "unpacked directories" as if though they were packaged extensions</sub>

3. Click on "Load unpacked" to load an extension 

3. You will be prompted to choose a file / folder. Select the folder `description`

4. The extension is now installed 
