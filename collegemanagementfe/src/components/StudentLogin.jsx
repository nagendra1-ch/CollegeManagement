
import React, { useEffect, useState } from 'react'
import '../styles/Login.css'
import { replace, useNavigate } from 'react-router-dom'
import axios from 'axios'


const StudentLogin = () => {
    const navigate=useNavigate()

  const [details, setDetails] = useState({
    email: '',
    password: ''
  })
  useEffect(()=>{
    const access=localStorage.getItem('access-token')
    if(access){
      navigate('/home',{replace:true})
    }
  },[navigate])

  
    const handleClick=()=>{
      navigate('/register')
    }

  const handleSubmit = async (e) => {
    e.preventDefault()
    try {
    const response = await axios.post(
        "http://localhost:8000/api/student-login",details
    );
    const res=response.data
    localStorage.setItem('access-token',res.access)
    localStorage.setItem('refresh-token',res.refresh)
    navigate('/home')
    

    } catch (error) {
        console.log("Status:", error.response?.status);
        console.log("Django error:", error.response?.data);
    }
    

  }

  

  return (
    <>

    
       <div className="login-card">
      <form onSubmit={handleSubmit}>
        <h2>Login</h2>
        <input 
          name="email" 
          type="email" 
          placeholder="Please enter email" 
          onChange={(e) => setDetails({ ...details, [e.target.name]: e.target.value })} 
        />
        <input 
          name="password" 
          type="password" 
          placeholder="Please enter password" 
          onChange={(e) => setDetails({ ...details, [e.target.name]: e.target.value })} 
        />
        <button type="submit">Login</button>
      </form>
      <p>
        Don't have an account? <button onClick={handleClick} type="button" className="register-btn">Register</button>
      </p>
    </div>
  </>
  )
}

export default StudentLogin