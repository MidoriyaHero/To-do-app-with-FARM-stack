import React from 'react'

export const publicRoute = (props) => {
    const {children} = props;
    const auth = useAuth();
    const navigate = useNavigate();
    const location = useLocation();
    const [isVerified, setIsVerified] = useState(false);
    
    useEffect(() => {
        if (!auth.isAuthenticated) {
            navigate('/login', {replace: true, state:{from: location}});
        } else {
            setIsVerified(true);
        }
    }, [auth.isAuthenticated, location, navigate]);
    if (!isVerified) {
        return null;
    }
    return (
        <>{children}</>
  )
}
