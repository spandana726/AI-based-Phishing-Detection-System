document.addEventListener("DOMContentLoaded", function () {
    const checkButton = document.getElementById("checkButton");
    const resultDiv = document.getElementById("result");
    const urlInput = document.getElementById("urlInput");

    checkButton.addEventListener("click", function () {
        let url = urlInput.value.trim();
        if (!url) {
            resultDiv.innerHTML = "<span style='color:red;'>⚠️ Please enter a URL!</span>";
            return;
        }

        resultDiv.innerHTML = "🔄 Checking URL..."; // Loading indicator

        fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ url: url }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                resultDiv.innerHTML = `<span style='color:red;'>❌ Error: ${data.error}</span>`;
            } else {
                let status = data.phishing ? "<b>Phishing 🚨</b>" : "<b>Safe ✅</b>";
                let confidence = (data.confidence * 100).toFixed(2);
                resultDiv.innerHTML = `${status} (Confidence: ${confidence}%)`;
            }
        })
        .catch(error => {
            resultDiv.innerHTML = "<span style='color:red;'>❌ API Error! Check if Flask is running.</span>";
            console.error("API Error:", error);
        });
    });
});
