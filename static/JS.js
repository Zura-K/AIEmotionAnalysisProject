let RunSentimentAnalysis = () => {
    let textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && (this.status == 200 || this.status == 400)) {
            let response = JSON.parse(xhttp.responseText);
            let systemResponse = document.getElementById("system_response");

            if (response.error) {
                systemResponse.innerHTML = `<div class="error">❌ Error: ${response.error}</div>`;
            } else {
                let result = response.response;
                systemResponse.innerHTML = `
                    <div class="result-box">
                        <p><strong>Analyzed Text:</strong> "${textToAnalyze}"</p>
                        <p><strong>System Response:</strong></p>
                        <div class="response">${result}</div>
                    </div>`;
            }
        }
    };

    xhttp.open("GET", "emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze), true);
    xhttp.send();
};
