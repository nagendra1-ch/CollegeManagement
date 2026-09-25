import React from 'react'
import { useNavigate } from 'react-router-dom'

const Logout = () => {
    localStorage.clear()
    const navigate=useNavigate()
    navigate('/login')
    
  return (
    <> Logged out successfully</>
  )

}

export default Logout