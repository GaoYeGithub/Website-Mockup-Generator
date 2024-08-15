const resultImg = document.getElementById("resultImg");
const Download = document.getElementById("Download");
const loading = document.getElementById("loading");

const generateMockup = () => {
  const websiteAddress = document.getElementById("websiteAddress").value;
  const bgColor = document.getElementById("bgColor").value;
  const mockup =
    "https://2s9e3bif52.execute-api.eu-central-1.amazonaws.com/production/screenshot?url=" +
    websiteAddress +
    "&color=" +
    bgColor;

  loading.style.display = 'block';

  resultImg.src = mockup;

  resultImg.onload = () => {
    loading.style.display = 'none';
  };

  Download.addEventListener("click", () => {
    window.open(mockup);
  });
};
