import React, { useState } from "react";

function PaperUpload({ onSubmit }) {
  const [file, setFile] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = () => {
    if (file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        onSubmit(e.target.result);
      };
      reader.readAsText(file);
    }
  };

  return (
    <div>
      <input type="file" accept=".txt,.pdf" onChange={handleFileChange} />
      <button onClick={handleSubmit}>Upload and Process</button>
    </div>
  );
}

export default PaperUpload;
