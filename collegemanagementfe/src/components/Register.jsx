import React, { useState } from 'react'
import Login from './Login'
import { useNavigate } from 'react-router-dom'
import "../styles/Register.css"
import axios from 'axios'


const Register = () => {
  const [data, setData] = useState({
    first_name: '',
    last_name: '',
    email: '',
    age: '',
    gender: '',
    branch: '',
    // date_of_join: '',
    phone: '',
    password: '',
    Fid:'',
    
  })

  const navigate=useNavigate()

  const handleClick=()=>{
    navigate('/login')
  }

  const handleChange = (e) => {
    setData({
      ...data,
      [e.target.name]: e.target.value
    })
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    console.log(data)

    try {
    const response = await axios.post(
        "http://localhost:8000/api/faculty-register",data
    );

    console.log("Success:", response.data);
    navigate('/login')

    } catch (error) {
        console.log("Status:", error.response?.status);
        console.log("Django error:", error.response?.data);
    }
  }

  return (
    <div className="register-container">
      <h2>Register</h2>
      <form onSubmit={handleSubmit}>
        <input 
          type="text" 
          name="first_name" 
          placeholder="Enter first name" 
          value={data.first_name}
          onChange={handleChange} 
        />
        <input 
          type="text" 
          name="last_name" 
          placeholder="Enter last name" 
          value={data.last_name}
          onChange={handleChange} 
        />
        <input 
          type="email" 
          name="email" 
          placeholder="Enter email" 
          value={data.email}
          onChange={handleChange} 
        />
        <input 
          type="number" 
          name="age" 
          placeholder="Enter age" 
          value={data.age}
          onChange={ (e) => {setData({...data,[e.target.name]: Number(e.target.value)})} }/>
        {/* <input 
          type="date" 
          name="date_of_join" 
          value={data.date_of_join}
          onChange={handleChange} 
        /> */}
        <input 
          type="text" 
          name="phone" 
          placeholder="Enter phone number" 
          value={data.phone}
          onChange={handleChange} 
        />
        <input 
          type="text" 
          name="Fid" 
          placeholder="Enter Faculty ID" 
          value={data.Fid}
          onChange={handleChange} 
        />
        <input 
          type="password" 
          name="password" 
          placeholder="Enter password" 
          value={data.password}
          onChange={handleChange} 
        />
        
        <select name="gender" value={data.gender} onChange={handleChange}>
          <option value="">Select Gender</option>
          <option value="male">Male</option>
          <option value="female">Female</option>
        </select>

        <select name="branch" value={data.branch} onChange={handleChange}>
          <option value="">Select Branch</option>
          <option value="CAD">CAD</option>
          <option value="CSE">CSE</option>
          <option value="CIVIL">Civil</option>
          <option value="ECE">ECE</option>
          <option value="MECH">Mech</option>
          <option value="EEE">EEE</option>
        </select>

        <button type="submit">Register</button>
      </form>
      <p>
        Already have an account? < button onClick={handleClick} type="button" className="login-link-btn">Login</button>
      </p>
    </div>
  )
}

export default Register