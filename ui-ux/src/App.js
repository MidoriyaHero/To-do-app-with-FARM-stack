import {BrowserRouter as Router, Route, Routes, Navigate} from "react-router-dom";
import {Login} from "./components/auths/login";
import {Register} from "./components/auths/register";
import {AuthProvider, AuthConsumer} from './context/JWTAuthContext'
import { Spinner } from "@chakra-ui/react";

function App() {
  return (
    <>
    <AuthProvider>
    <Router>
      <AuthConsumer>
        {(auth)=> !auth.isInitialized? (
          <Flex height = '100vh' alignItems = 'center' justifyContent = 'center'>
            <Spinner thickness='4px' speed='0.5s' emptyColor='green.200' color="green.500" />
          </Flex>
        ): (
          <Routes>
          <Route path='/login' element ={<Login />} />
          <Route path='/register' element ={<Register />} />
          <Route path='/' element ={<h1>HOME PAGE</h1>} />
          <Route path='*' element ={<Navigate to ='/' />} />
        </Routes>
        )}
      </AuthConsumer>
    </Router>
    </AuthProvider>
    </>
  );
}

export default App;
