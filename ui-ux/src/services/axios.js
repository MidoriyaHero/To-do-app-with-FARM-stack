import axios from 'axios';

const baseURL = 'http://localhost:8000/api/';

export const axiosInstance = axios.create({
    baseURL
});

axiosInstance.interceptors.response.use(
    (response) => response, 
    (error) => {
        return Promise.reject(error);
    }
);

export default axiosInstance;