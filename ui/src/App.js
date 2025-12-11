import { useState } from "react";

function App() {
  const [age, setAge] = useState("");
  const [marks, setMarks] = useState("");
  const [result, setResult] = useState(null);

  const handlePredict = async () => {
    // const url = `http://127.0.0.1:8000/predict?age=${age}&marks=${marks}`;
        const url = `https://student-ml-api.onrender.com/predict?age=${age}&marks=${marks}`;


    try {
      const response = await fetch(url);
      const data = await response.json();
      setResult(data);
    } catch (error) {
      console.error("API Error: ",error);
      alert("Error connecting to API");
    }
  };

  return (
    <div style={{ padding: "40px", maxWidth: "400px" }}>
      <h2>Student Performance Predictor</h2>

      <label>Age:</label>
      <input
        type="number"
        value={age}
        onChange={(e) => setAge(e.target.value)}
      />

      <br /><br />

      <label>Marks:</label>
      <input
        type="number"
        value={marks}
        onChange={(e) => setMarks(e.target.value)}
      />

      <br /><br />

      <button onClick={handlePredict}>Predict</button>

      {result && (
        <div style={{ marginTop: "20px" }}>
          <h3>Prediction Result:</h3>
          <p><b>Predicted Label:</b> {result.predicted_label}</p>
          <p><b>Probabilities:</b></p>
          <ul>
            <li>Low: {result.probabilities.Low}</li>
            <li>Medium: {result.probabilities.Medium}</li>
            <li>High: {result.probabilities.High}</li>
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;