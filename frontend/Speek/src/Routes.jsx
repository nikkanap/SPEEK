import { Route, createBrowserRouter, createRoutesFromElements, RouterProvider } from 'react-router-dom';
import Home from './pages/Home';
import Login from './pages/auth/Login';
import Signup from './pages/auth/Signup'; 

// router for creating the browser routes
const router = createBrowserRouter(
  createRoutesFromElements(
    <> 
      <Route path='/' element={<Home />} /> 
      <Route path='/login' element={<Login />} />
      <Route path='/signup' element={<Signup />} />
    </>
  )
)


// Where the app is
const AppRoutes = () => {
  return (
    <>
      <RouterProvider router={router} />
    </>
  );
}

export default AppRoutes