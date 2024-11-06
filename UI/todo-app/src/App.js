import {
  BrowserRouter as Router,

  Route,
  Routes,
} from "react-router-dom";

import {login} from './components/login';
function App() {
  return <Router>
    <Routes>
      <Route path ="/login" element={login} />
      <Route path ="/register" element={<h1>Register</h1>} />
    </Routes>
  </Router>
}

export default App;
