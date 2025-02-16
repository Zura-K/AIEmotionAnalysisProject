let RunSentimentAnalysis = () => {
    let textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            let response = JSON.parse(xhttp.responseText);
            let systemResponse = document.getElementById("system_response");

            if (response.error) {
                systemResponse.innerHTML = `<p class="error">Error: ${response.error}</p>`;
            } else {
                let emotions = response.response.match(/'([^']+)': ([0-9.]+)/g)
                    .map(e => e.replace(/'/g, "").split(": "));

                let dominantEmotion = response.response.match(/The dominant emotion is (\w+)\./)[1];

                let htmlOutput = `<h3>Sentiment Analysis Result</h3>`;
                htmlOutput += `<p><strong>Analyzed Text:</strong> "${textToAnalyze}"</p>`;
                htmlOutput += `<ul>`;

                emotions.forEach(([emotion, value]) => {
                    htmlOutput += `<li><strong>${emotion}:</strong> ${parseFloat(value).toFixed(4)}</li>`;
                });

                htmlOutput += `</ul>`;
                htmlOutput += `<p class="dominant-emotion">The dominant emotion is: <strong>${dominantEmotion}</strong></p>`;

                systemResponse.innerHTML = htmlOutput;
            }
        }
    };

    xhttp.open("GET", "emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze), true);
    xhttp.send();
};
