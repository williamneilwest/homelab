import { useState, useEffect } from "react";
import { BrowserRouter as Router, Route, Routes, Navigate } from "react-router-dom";
import Login from "./Login";
import Dashboard from "./Dashboard";
import jwtDecode from "jwt-decode";

const App = () => {
  const [token, setToken] = useState(localStorage.getItem("token"));

  useEffect(() => {
    if (token) {
      const decoded = jwtDecode(token);
      if (!decoded || decoded.exp * 1000 < Date.now()) {
        setToken(null);
        localStorage.removeItem("token");
      }
    }
  }, [token]);

  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login setToken={setToken} />} />
        <Route path="/dashboard" element={token ? <Dashboard /> : <Navigate to="/login" />} />
      </Routes>
    </Router>
  );
};

export default App;
