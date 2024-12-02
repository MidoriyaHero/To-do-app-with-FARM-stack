import { useEffect, useRef, useState } from "react"
import { useNavigate, useParams } from "react-router"
import  axiosInstance  from '../../services/axios'
import { Button, Center, Container, Spinner, Text } from "@chakra-ui/react"
import { CRUDTodo } from "./CRUDTodo"

export const TodoDetail = () => {
    const [todo, setTodo] = useState({})
    const [loading, setLoading] = useState(true)
    const isMounted = useRef(false)
    const {todoId} = useParams()
    const navigate = useNavigate()

    useEffect(() =>{
        if (isMounted.current) return;
        fetchTodo();
        isMounted.current = true
    }, [todoId])

    const fetchTodo = () => {
        setLoading(true)
        axiosInstance.get(`/todo/${todoId}`)
        .then((response) =>{
            setTodo(response.data)
        })
        .catch((error) => console.log(error))
        .finally(() => {
            setLoading(false)
        })
    }
    if (loading) {
        return (
            <Container>
                <Center mt={6} >
                    <Spinner thickness='4px' speed='0.5s' emptyColor='green.200' color="green.500" />
                </Center>
            </Container>
        )
    }
    return (
        <>
      <Container mt={6}>
        <Button
          colorScheme="yellow"
          onClick={() => navigate("/", { replace: true })}
        >
          Back
        </Button>
      </Container>
      <Container
        bg='orange'
        minHeight="7rem"
        my={3}
        p={3}
        rounded="lg"
        alignItems="center"
        justifyContent="space-between"
      >
        <Text fontSize={22}>{todo.title}</Text>
        <Text bg="gray.500" mt={2} p={2} rounded="lg">
          {todo.description}
        </Text>
        <CRUDTodo
          my={3}
          editable={true}
          defaultValues={{
            title: todo.title,
            description: todo.description,
            status: todo.status,
          }}
          onSuccess={fetchTodo}
        />
        </Container>
        </>
    )
}
