
async function sendQuestion() {
  const input = document.getElementById("userInput").value;
  const responseDiv = document.getElementById("response");
  responseDiv.textContent = "Thinking...";

  const res = await fetch("/ask", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ question: input })
  });

  const data = await res.json();
  responseDiv.textContent = data.reply;
}
