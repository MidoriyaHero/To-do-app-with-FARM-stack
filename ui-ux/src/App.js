import {BrowserRouter as Router, Route, Routes} from "react-router-dom";
import {Login} from "./components/auths/login";
import {Register} from "./components/auths/register";

function App() {
  return (
    
    <Router>
      <Routes>
        <Route path='/login' element ={<Login />} />
        <Route path='/register' element ={<Register />} />
      </Routes>
    </Router>
  );
}

export default App;
