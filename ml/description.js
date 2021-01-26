var ml_endpoint = "https://greenturtle.herokuapp.com/predict"; 
var images = document.getElementsByTagName("img");
var dev = false;

function insert_alt(image, endpoint, request_options){
    let alt_text = "";
    if (dev) {
        endpoint = "https://cors-anywhere.herokuapp.com/" + endpoint;
    }
	fetch(endpoint,request_options)
		.then(response => response.json())
		.then(result => {
			image.alt = result['prediction'];
            console.log(image.alt)
		})
		.catch(error => console.log(error));
}

for(i = 0; i < images.length; i++){
	var src = images[i].src;
	var image_url = src;
    
    if (!images[i].alt && (image_url.includes("png") || image_url.includes("jpg"))) {
        if(!image_url.startsWith("http")){
            image_url = window.location.protocol + "//" + window.location.host + src;
        }

        var imagenode = images[i];
        
        var myHeaders = new Headers();
        myHeaders.append("Access-Control-Allow-Origin", "*");
        myHeaders.append("Accept", "application/json");

        var formdata = new FormData();
        formdata.append("data", image_url);

        var requestOptions = {
            method: 'POST',
            headers: myHeaders,
            body: formdata,
            rejectUnauthorized: false
        };

        var d = new Date();
        var n = d.toLocaleTimeString();

        console.log(n);

        insert_alt(images[i], ml_endpoint, requestOptions);
    }
}
