var ml_endpoint = "https://0.0.0.0:5000/predict"; 
var images = document.getElementsByTagName("img");

function insert_alt(image, endpoint, request_options){
    let alt_text;
	fetch(endpoint,request_options)
		.then(response => response.json())
		.then(result => {
			console.log(result);
			alt_text = result['prediction'];
		})
		.catch(error => console.log(error));
    image.alt = alt_text;
}

for(i = 0; i < images.length; i++){
	var src = images[i].src;
	var image_url = src;
	if(!image_url.startsWith("http")){
		image_url = window.location.protocol + "//" + window.location.host + src;
	}
	var imagenode = images[i];
	var alt_text;
	
	var myHeaders = new Headers();
	myHeaders.append("Accept", "application/json");
	myHeaders.append("Access-Control-Allow-Origin", "*");

	var formdata = new FormData();
	formdata.append("data", image_url);

	var requestOptions = {
		method: 'POST',
		headers: myHeaders,
		mode: 'no-cors',
		body: formdata,
        rejectUnauthorized: false
	};

    var d = new Date();
    var n = d.toLocaleTimeString();

    console.log(n);

	insert_alt(images[i], ml_endpoint, requestOptions);
}
