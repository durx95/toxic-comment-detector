async function predict() {
    const text = document.getElementById("textInput").value;
    const resultBox = document.getElementById("resultBox");
    const resultText = document.getElementById("resultText");
    const loader = document.getElementById("loader");

    if (!text.trim()) {
        alert("Please enter some text");
        return;
    }

    resultBox.classList.add("hidden");
    loader.classList.remove("hidden");

    try {
        const response = await fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ text: text })
        });

        const data = await response.json();

        loader.classList.add("hidden");
        resultBox.classList.remove("hidden");

        if (data.prediction === 1) {
            resultBox.className = "result toxic";
            resultText.innerText = "⚠️ Toxic Comment";
        } else {
            resultBox.className = "result clean";
            resultText.innerText = "✅ Not Toxic";
        }

    } catch (error) {
        loader.classList.add("hidden");
        alert("Error connecting to server");
    }
}