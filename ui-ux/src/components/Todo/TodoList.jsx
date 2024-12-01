import { Box, Center, Container, Spinner } from '@chakra-ui/react'
import React, { useEffect, useRef, useState } from 'react'
import axiosInstance from '../../services/axios';
import { TodoCard } from './TodoCard';

export const TodoList = () => {
    const [todos, setTodos] = useState([]);
    const [loading, setLoading] = useState(true);
    const isMounted = useRef(false);
    useEffect(() => {
        if (isMounted.current) return;
        fetchTodo();
        isMounted.current = true
    }, [])

    const fetchTodo = () => {
        setLoading(true)
        axiosInstance.get('/todo')
        .then((response) =>{
            setTodos(response.data)
        }).catch ((error) => {
            console.log(error)
        }).finally(() => {
            setLoading(false)
        })
    }
    return (
    <Container mt={9}  >
        {loading ? (
            <Center mt={6} >
                <Spinner thickness='4px' speed='0.5s' emptyColor='green.200' color="green.500" />
            </Center>
        ):(
            <Box mt={6}>
                {todos?.map((todo) =>(
                    <TodoCard todo = {todo} key = {todo.id}/>
                ))}
            </Box>
        )}
    </Container>
    )
}
