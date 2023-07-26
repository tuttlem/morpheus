import React from 'react';
import ReactDOM from 'react-dom/client';

import 'bootstrap/dist/css/bootstrap.min.css';
import './assets/css/bootstrap.min.css';
import 'react-toastify/dist/ReactToastify.css'
import "./index.css"

import {BrowserRouter as Router, Route, Routes} from "react-router-dom";
import Layout from "./Layout";
import Dashboard from "./pages/Dashboard";
import Competitions from "./pages/Competitions";
import Stadiums from "./pages/Stadiums";

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Dashboard />} />
          <Route path="/competitions" element={<Competitions />} />

          <Route path="/stadiums" element={<Stadiums />}>
            <Route path=":id"  element={<Stadiums />} />
          </Route>

        </Route>
      </Routes>
    </Router>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
