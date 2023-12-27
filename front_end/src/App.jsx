import { useState } from "react";

function App() {
  const [file, setFile] = useState([]);

  const handleFileChange = (e) => {
    if (e.target.files) {
      setFile(e.target.files[0]);
    }
  };

  const handleFileUpload = () => {
    if (!file) {
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    fetch("http://127.0.0.1:5000/submit_cv", {
      method: "POST",
      body: formData,
    })
      .then((res) => res.json())
      .then((data) => console.log(data))
      .catch((err) => console.error(err));
  };

  return (
    <>
      <input type="file" onChange={handleFileChange} />
      <div>{file.name}</div>
      <button onClick={handleFileUpload}>Upload CV</button>
    </>
  );
}

export default App;
