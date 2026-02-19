document.addEventListener("DOMContentLoaded", () => {
  const dropArea = document.getElementById("drop-area");
  const fileInput = document.getElementById("file-input");
  const gallery = document.getElementById("gallery");

  ["dragenter", "dragover", "dragleave", "drop"].forEach((eventName) => {
    dropArea.addEventListener(
      eventName,
      (e) => {
        e.preventDefault();
        e.stopPropagation();
      },
      false,
    );
  });

  ["dragenter", "dragover"].forEach((eventName) => {
    dropArea.addEventListener(
      eventName,
      () => dropArea.classList.add("highlight"),
      false,
    );
  });

  ["dragleave", "drop"].forEach((eventName) => {
    dropArea.addEventListener(
      eventName,
      () => dropArea.classList.remove("highlight"),
      false,
    );
  });

  dropArea.addEventListener(
    "drop",
    (e) => {
      const dt = e.dataTransfer;
      const files = dt.files;

      if (files && files.length > 0) {
        fileInput.files = files;
        handleFile(files[0]);
      }
    },
    false,
  );

  dropArea.addEventListener("click", () => {
    fileInput.click();
  });

  fileInput.addEventListener("change", function () {
    if (this.files && this.files[0]) {
      handleFile(this.files[0]);
    }
  });

  function handleFile(file) {
    if (!file.type.startsWith("image/")) {
      return;
    }

    const reader = new FileReader();

    const label = dropArea.querySelector("p");
    if (label) label.innerText = `Loading...`;

    reader.onload = (e) => {
      gallery.innerHTML = "";
      const img = document.createElement("img");
      img.src = e.target.result;
      img.style.maxWidth = "100%";
      img.style.display = "block";
      img.style.margin = "10px auto";
      gallery.appendChild(img);

      if (label) label.innerText = ``;
    };

    reader.readAsDataURL(file);
  }
});
