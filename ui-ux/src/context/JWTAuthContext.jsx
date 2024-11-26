import {createContext} from 'react'
import {userReducer} from 'react'
import {validateToken} from  '../utils/jwt'
const initialState = {
    isAuthenticated: false,
    isInitialized: false,
    user: null,
}

export const AuthContext = createContext({
    ...initialState,
    login: () => Promise.resolve(),
    logout: () => Promise.resolve(),

});

const handlers = {
    INITIALIZE: (state, action) => {
        const {isAuthenticated, user} = action.payload;
        return {
            ...state,
            isAuthenticated,
            isInitialized: true,
            user,
        };
    },

    LOGIN: (state, action) => {
        const {user} = action.payload;
        return {
            ...state,
            isAuthenticated: true,
            user,
        };
    },
    LOGOUT: (state) => {
        return {
            ...state,
            isAuthenticated: false,
            user: null,
        };
    },
};

const reducer = (state, action) =>  
    handlers[action.type] ? handlers[action.type](state, action) : state

const AuthProvider = (props) => {
    const {children} = props;
    const [state, dispatch] = userReducer(reducer, initialState)
    const initialize = async () => {
        try {
            const accessToken = localStorage.getItem('accessToken')
            if (accessToken && validateToken(accessToken)) {
                
            }
        } catch (err) {

        }
    }
}