var KEY =  "881d410edc88957"
var ocr_endpoint = "https://api.ocr.space/parse/image?apikey="+KEY;
var ml_endpoint = "https://greenturtle.herokuapp.com/predict"; 
var images = document.getElementsByTagName("img");

async function ocr_request(endpoint){
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

    var ocr_text = await fetch(endpoint, requestOptions)
		.then(response => response.json())
		.then(result => {
			return result['ParsedResults'][0]['ParsedText'];
		})
		.catch(error => console.log(error))
		.catch(error => {
            console.log(error);
            return "";
        });

    // console.log(ocr_text);
    return ocr_text;
}

async function ml_request(endpoint){
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

	var prediction = await fetch(endpoint, requestOptions)
		.then(response => response.json())
		.then(result => {
			// console.log(result);
			return result['prediction'];
		})
		.catch(error => console.log(error));

    // console.log(prediction);
    return prediction;
}

async function insert_alt(image){
    console.log("insert alt");
    var prediction = await ml_request(ml_endpoint);
    // console.log("prediction: " + prediction);
    var ocr_text = await ocr_request(ocr_endpoint);
    // console.log("ocr: " + ocr_text);

    var alt_text = prediction + " " + ocr_text; 
    console.log(alt_text);

    image.alt = alt_text;
}

for(i = 0; i < images.length; i++){
	var src = images[i].src;
	var image_url = src;
	if(!image_url.startsWith("http")){
		image_url = window.location.protocol + "//" + window.location.host + src;
	}
	var imagenode = images[i];
	

	insert_alt(images[i]);
}

