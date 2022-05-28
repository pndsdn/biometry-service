let video = document.querySelector("#videoElement");
let loadCircle = document.querySelector(".cssload-container");
let inputFile = document.querySelector("#upload-file");
let submitButton = document.querySelector("#submit-file");

inputFile.addEventListener("change", uploadFile, false);
submitButton.addEventListener("click", processingFile, false)

function uploadFile(e) {
    if (this.files && this.files.length === 1) {
        submitButton.className = 'active';
        submitButton.disabled = false;
        document.querySelector('#upload-file-text').textContent = 'File selected';
        document.querySelector('#upload-file-button').className ='selected-file';
    } else {
        submitButton.className = 'inactive';
        submitButton.disabled = true;
        document.querySelector('#upload-file-text').textContent = 'Choose file';
        document.querySelector('#upload-file-button').className = 'unselected-file';
        loadCircle.style.visibility = 'hidden';
    }
}

function processingFile(e) {
    submitButton.className = 'inactive';
    submitButton.value = 'Processing';
    loadCircle.style.visibility = 'visible';
    document.querySelector('#upload-file-text').textContent = 'Choose file';
    document.querySelector('#upload-file-button').className = 'unselected-file';
}