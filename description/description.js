var KEY =  "881d410edc88957"
var endpoint = "https://api.ocr.space/parse/image?apikey="+KEY;
var images = document.getElementsByTagName("img");

function insert_alt(image, endpoint, request_options){
	fetch(endpoint, requestOptions)
		.then(response => response.json())
		.then(result => {
			console.log(result);
			var alt_text = result['ParsedResults'][0]['ParsedText'];
			image.alt = alt_text;
		})
		.catch(error => console.log(error));
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
	myHeaders.append("apikey", KEY);
	myHeaders.append("Accept", "application/json");
	myHeaders.append("Access-Control-Allow-Origin", "*");

	var formdata = new FormData();
	formdata.append("language", "eng");
	formdata.append("isOverlayRequired", "false");
	formdata.append("url", image_url);
	formdata.append("iscreatesearchablepdf", "false");
	formdata.append("issearchablepdfhidetextlayer", "false");
	formdata.append("OCREngine","2");

	var requestOptions = {
		method: 'POST',
		headers: myHeaders,
		mode: 'cors',
		body: formdata,
		redirect: 'follow'
	};

	insert_alt(images[i], endpoint, requestOptions);
}
