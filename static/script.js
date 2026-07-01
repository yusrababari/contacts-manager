document.getElementById("runBtn").addEventListener("click", async () => {
  const input = document.getElementById("userInput").value;

  const response = await fetch("/api/run", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ input: input })
  });

  const data = await response.json();
  document.getElementById("output").textContent = data.result;
});