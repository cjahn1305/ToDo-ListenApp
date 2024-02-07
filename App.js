import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LoginPage from "./LoginPage";
import TodoListPage from "./TodoListPage"; // Annahme: Du hast eine Seite für die ToDo-Liste

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<LoginPage />} />
        <Route path="/todos" element={<TodoListPage />} />
        {/* Weitere Routen für andere Seiten */}
      </Routes>
    </Router>
  );
}

export default App;
