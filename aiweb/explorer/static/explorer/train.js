if (!localStorage.getItem('response_image')) {
  localStorage.setItem('response_image', 0)
};

function previewImages() {

    var preview = document.querySelector('#preview');

    // remove all child elements before appending
    preview.innerHTML = '';
    
    if (this.files) {
      [].forEach.call(this.files, readAndPreview);
    }
  
    function readAndPreview(file) {

      var reader = new FileReader();
      
      reader.addEventListener("load", function() {
        var image = new Image();
        image.height = 100;
        image.title = file.name;
        image.src = this.result;
        preview.appendChild(image);
      });
      
      reader.readAsDataURL(file);
      
    }
  
  };

function formValidation() {
  if (document.querySelector('#img-selector').value == "") {
    alert('Please choose at least one image');
    return false;
  } else if (document.querySelector('#jsonfile').value == "") {
    alert('Please choose a json file');
    return false;
  } else {
    localStorage.setItem('response_image',1);
    return true
  }
    
};

function formValidation2() {
  let response_image = parseInt(localStorage.getItem('response_image'),10);
  if (response_image===0) {
    alert('Please upload images before training');
    return false
  }
}

document.addEventListener('DOMContentLoaded',function() {
  document.querySelector('#img-selector').addEventListener("change", previewImages);

  let form = document.querySelector('#form1');
  form.onsubmit = formValidation;

  let form2 = document.querySelector('#form2');
  form2.onsubmit = formValidation2;

});

