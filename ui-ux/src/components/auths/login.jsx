import {
    Flex, 
    FormControl, 
    FormErrorMessage,
    Heading,
    Input
} from '@chakra-ui/react';
import {
    useForm
} from 'react-hook-form'
export const Login = () => {
    const {
        handleSumit,
        register,
        formState: {errors, isSubmit
        } = useForm();
    }
const onSubmit = (values) => {
    console.log(values)
}
    return <Flex height='100vh' align ='center' justifyContent='center'>
        <Flex 
        direction='column' 
        alignItems ='center' 
        background={('gray.100', 'gray.700')}
        p={12}
        rounded={6}>
            <Heading mb={6}>Login</Heading>
            <form onSubmit={handleSumit(onSubmit)}>
                <FormControl isInvalid={errors.email}>
                    <Input
                    placeholder='Email'
                    background={('gray.300', 'gray.600')}
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
            </form>
        </Flex>
        </Flex>
}