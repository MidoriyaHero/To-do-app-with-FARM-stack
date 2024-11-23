import {
    Button,
    Flex, 
    Heading,
    Input} from '@chakra-ui/react';
import {
    FormControl, 
    FormErrorMessage,
} from '@chakra-ui/form-control';
import {useForm} from 'react-hook-form'
import { useNavigate } from "react-router";
import {ThemeToggle} from '../theme/ThemeToggle'

export const Login = () => {
    const {
        handleSubmit,
        register,
        formState: {errors, isSubmitting,},
    }  = useForm();

    const navigate = useNavigate();

    const onSubmit = (values) => {
        console.log(values)
    }
    return <Flex height='100vh' align ='center' justifyContent='center'>
        <Flex 
        direction='column' 
        alignItems ='center' 
        background={('orange.200')}
        p={12}
        rounded={6}>
            <Heading textColor='orange' mb={6}>Login</Heading>
            <form onSubmit={handleSubmit(onSubmit)}>
                <FormControl isInvalid={errors.email}>
                    <Input
                    placeholder='Email'
                    background={('orange.100')}
                    type='email'
                    size='lg'
                    mt={6}
                    {...register('email',{
                        required: "This is required field!!!"
                    })}
                    />
                    <FormErrorMessage>
                        {errors.email && errors.email.message}
                    </FormErrorMessage>
                </FormControl>
                
                <FormControl isInvalid={errors.email}>
                    <Input
                    placeholder='Password'
                    background={('orange.100')}
                    type='password'
                    size='lg'
                    mt={6}
                    {...register('password',{
                        required: "This is required field!!!"
                    })}
                    />
                    <FormErrorMessage>
                        {errors.password && errors.password.message}
                    </FormErrorMessage>
                </FormControl>

                <Button 
                isLoading={isSubmitting}
                loadingText='Logging in...'
                width='100%' colorScheme='orange' textColor='orange' variant='outline' mt={3} mb ={0}
                type = 'submit'>
                    Login
                </Button>
            </form>

            <Button 
            onClick={()=> navigate('/register', {replace:true})} 
            width='100%' colorScheme='orange' textColor='orange.300' variant='link' mt={3} mb={2}>
                Or Register
            </Button>
            <ThemeToggle showLable={true}/>
        </Flex>
        </Flex>
}