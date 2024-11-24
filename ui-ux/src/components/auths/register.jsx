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

export const Register = () => {
    const {
      handleSubmit,
      register,
      formState: { errors, isSubmitting },
    } = useForm();
    const navigate = useNavigate();
    
    const onSubmit = (values) => {
        console.log(values)
    }
    return (
      <Flex height="100vh" alignItems="center" justifyContent="center">
        <Flex
          direction="column"
          alignItems="center"
          background={('orange.200')}
          p={12}
          rounded={6}
        >
          <Heading mb={6}>Register</Heading>
          <form onSubmit={handleSubmit(onSubmit)}>
            <FormControl isInvalid={errors.email}>
              <Input
                placeholder="Email"
                background={('orange.100')}
                type="email"
                size="lg"
                mt={6}
                {...register("email", {
                  required: "This is required field",
                })}
              />
              <FormErrorMessage>
                {errors.email && errors.email.message}
              </FormErrorMessage>
            </FormControl>
            <FormControl isInvalid={errors.username}>
              <Input
                placeholder="username"
                background={('orange.100')}
                type="text"
                variant="filled"
                size="lg"
                mt={6}
                {...register("username", {
                  required: "This filed is required",
                  minLength: {
                    value: 5,
                    message: "Username must be at least 5 characters",
                  },
                  maxLength: {
                    value: 24,
                    message: "Username must be at most 24 characters",
                  },
                })}
              />
              <FormErrorMessage>
                {errors.username && errors.username.message}
              </FormErrorMessage>
            </FormControl>
            <FormControl isInvalid={errors.email}>
              <Input
                placeholder="Password"
                background={('orange.100')}
                type="password"
                size="lg"
                mt={6}
                {...register("password", {
                  required: "This is required field",
                  minLength: {
                    value: 5,
                    message: "Password must be at least 5 characters long",
                  },
                  maxLength: {
                    value: 24,
                    message: "Password must be at most 24 characters",
                  },
                })}
              />
              <FormErrorMessage>
                {errors.password && errors.password.message}
              </FormErrorMessage>
            </FormControl>
            <Button
              isLoading={isSubmitting}
              loadingText="Creating account..."
              width="100%"
              colorScheme="green"
              variant="outline"
              mt={6}
              mb={6}
              type="submit"
            >
              Register
            </Button>
          </form>
          <ThemeToggle showLabel={true} />
          <Button
            onClick={() => navigate("/login", { replace: true })}
            width="100%"
            colorScheme="gray"
            variant="outline"
            mt={6}
          >
            Login Instead
          </Button>
        </Flex>
      </Flex>
    );
  };