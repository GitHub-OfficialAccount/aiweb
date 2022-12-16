document.addEventListener('DOMContentLoaded',function() {
    document.querySelector('#img-selector').addEventListener("change", previewImages);
});

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
  
  }
  