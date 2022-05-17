let video = document.querySelector("#videoElement");
let stopVideo = document.querySelector("#stop");
let startVideo = document.querySelector("#start");
let loadCircle = document.querySelector(".cssload-container");
let inputFile = document.querySelector("#upload-file");
let submitButton = document.querySelector("#submit-file");
let streamGo = false;

stopVideo.addEventListener("click", stop, false);
startVideo.addEventListener("click", startWebCam, false);
inputFile.addEventListener("change", uploadFile, false);

function startWebCam() {
	loadCircle.style.visibility = 'visible';
    if (navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({video: true})
                .then(function (stream) {
                    video.srcObject = stream;
                    streamGo = true;
                    loadCircle.style.visibility = 'hidden';
                })
                .catch(function (err0r) {
                    console.log("Something went wrong!");
                });
    }
}

function stop() {
    if (streamGo) {
        let stream = video.srcObject;
        let tracks = stream.getTracks();

        for (let i = 0; i < tracks.length; i++) {
            let track = tracks[i];
            track.stop();
        }
        streamGo = false;
        video.srcObject = null;
    }
}

function uploadFile(e) {
    stop();
    if (this.files && this.files.length === 1) {
        submitButton.className = 'active';
        submitButton.disabled = false;
        document.querySelector('#upload-file-text').textContent = 'File selected';
        document.querySelector('#upload-file-button').className ='selected-file';
    } else {
        submitButton.className = 'inactive';
        submitButton.disabled = true;
        document.querySelector('#upload-file-text').textContent = 'Choose file';
        document.querySelector('#upload-file-button').className ='unselected-file';
    }
}