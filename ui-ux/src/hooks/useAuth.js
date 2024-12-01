import {useContext} from 'reatc';
import { AuthContext } from '../context/JWTAuthContext';

export const useAuth = () => useContext(AuthContext);