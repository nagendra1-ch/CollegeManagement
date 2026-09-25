import { useState } from 'react'
import Login from './components/Login'
import Register from './components/Register'
import Logout from './components/Logout'
import Home from './components/Home'
import { Route,Routes } from 'react-router-dom'
import { useNavigate } from 'react-router-dom'
import StudentRegister from './components/StudentRegister'
import StudentProfile from './components/StudentProfile'
import StudentLogin from './components/StudentLogin'

function App() {
  const [count, setCount] = useState(0)
  const [islogin,setislogin]=useState(true)
  const navigate=useNavigate()
  const access_token=localStorage.getItem('access-token')
  
  




  return (
    <>
    <Routes>
      <Route path='/login' element={<Login/>}/>
      <Route path='/register' element={<Register/>}/>
      <Route path='/logout' element={<Logout/>}/>
      <Route path='/home' element={<Home/>} />
      <Route path='addstudent' element={<StudentRegister/>}/>
      <Route path='profile' element={<StudentProfile/>}/>
      <Route path='studentlogin' element={<StudentLogin/>}/>
    </Routes>


    

    

    

    
    </>
  )
}

export default App
