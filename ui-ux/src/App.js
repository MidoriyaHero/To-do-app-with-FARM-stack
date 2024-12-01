import { BrowserRouter as Router, Route, Routes, Navigate} from "react-router-dom";
import { Login} from "./components/auths/login";
import { Register} from "./components/auths/register";
import { AuthProvider, AuthConsumer} from './context/JWTAuthContext'
import { Spinner } from "@chakra-ui/react";
import { PublicRoute} from './components/auths/PublicRoute';
import { Authenticated} from './components/auths/Authenticated';
import { Flex } from '@chakra-ui/react';
import { TodoList } from "./components/Todo/TodoList";
import { NavBar } from "./components/NavBar/NavBar";

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
            <Route path='/login' element ={<PublicRoute> <Login /> </PublicRoute>} />
            <Route path='/register' element ={<PublicRoute> <Register /> </PublicRoute>} />
            <Route path='/' element={<NavBar/>} >
              <Route path='/' element ={<Authenticated> <TodoList/> </Authenticated>} />
            </Route>
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
