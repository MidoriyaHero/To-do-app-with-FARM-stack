import { Box, Button, Flex, Stack, Text } from '@chakra-ui/react'
import React from 'react'
import { ThemeToggle } from '../theme/ThemeToggle'
import { useAuth } from '../../hooks/useAuth'
import { Outlet } from 'react-router-dom'

export const NavBar = () => {
    const {logout} = useAuth();
    return (
        <Box minHeight='100vh'>
            <Flex as='nav' alignItems='center' justifyContent='space-between' wrap='wrap' p={2} bg ='orange.200' color='white' >
                <Text as='h2' fontSize={24} fontWeight='bold'  >
                    {" "}
                    TO DO LIST
                </Text>
                <Stack direction='row' align='center' spacing={4} >
                    <ThemeToggle/>
                    <Button onClick={logout} colorScheme='orange.200' >
                        Logout
                    </Button>
                </Stack>
            </Flex>
            <Outlet/>
        </Box>
    )
}
