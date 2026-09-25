import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import "../styles/StudentRegister.css"
import axios from 'axios'

const StudentRegister = () => {

  const [data, setData] = useState({
    first_name: '',
    last_name: '',
    email: '',
    age: '',
    gender: '',
    branch: '',
    phone: '',
    password: '',
    Sid: '',
    semister:'',
    year:'',

  })

  const navigate = useNavigate()

  const handleChange = (e) => {
    setData({
      ...data,
      [e.target.name]: e.target.value
    })
  }

  const handleSubmit = async (e) => {
  e.preventDefault();
  console.log(data);

  try {
    const token = localStorage.getItem("access-token");

    const response = await axios.post(
      "http://localhost:8000/api/student-register",
      data,
      {
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json",
        },
      }
    );

    console.log(response);
    console.log("Success:", response.data);

    alert("Student registered successfully!");

    setData({
      first_name: "",
      last_name: "",
      email: "",
      age: "",
      gender: "",
      branch: "",
      phone: "",
      password: "",
      Sid: "",
      year:'',
      semister:'',
    });

  } catch (error) {

    console.log("Status:", error.response?.status);
    console.log("Django error:", error.response?.data);

    alert(
      error.response?.data?.message ||
      "Student registration failed!"
    );
  }
};

  return (
    <div className="register-page">

      <div className="register-container">

        <div className="register-header">
          <div className="register-icon">
            🎓
          </div>

          <h2>Student Registration</h2>

          <p>
            Add a new student to the college management system
          </p>
        </div>

        <form onSubmit={handleSubmit}>

          <div className="form-grid">

            <div className="form-group">
              <label>First Name</label>

              <input
                type="text"
                name="first_name"
                placeholder="Enter first name"
                value={data.first_name}
                onChange={handleChange}
                required
              />
            </div>


            <div className="form-group">
              <label>Last Name</label>

              <input
                type="text"
                name="last_name"
                placeholder="Enter last name"
                value={data.last_name}
                onChange={handleChange}
                required
              />
            </div>


            <div className="form-group">
              <label>Email</label>

              <input
                type="email"
                name="email"
                placeholder="Enter email"
                value={data.email}
                onChange={handleChange}
                required
              />
            </div>


            <div className="form-group">
              <label>Age</label>

              <input
                type="number"
                name="age"
                placeholder="Enter age"
                value={data.age}
                onChange={(e) => {
                  setData({
                    ...data,
                    [e.target.name]: Number(e.target.value)
                  })
                }}
                required
              />
            </div>


            <div className="form-group">
              <label>Phone Number</label>

              <input
                type="text"
                name="phone"
                placeholder="Enter phone number"
                value={data.phone}
                onChange={handleChange}
                required
              />
            </div>


            <div className="form-group">
              <label>Student ID</label>

              <input
                type="text"
                name="Sid"
                placeholder="Enter Student ID"
                value={data.Sid}
                onChange={handleChange}
                required
              />
            </div>


            <div className="form-group">
              <label>Gender</label>

              <select
                name="gender"
                value={data.gender}
                onChange={handleChange}
                required
              >
                <option value="">Select Gender</option>
                <option value="male">Male</option>
                <option value="female">Female</option>
              </select>
            </div>


            <div className="form-group">
              <label>Branch</label>

              <select
                name="branch"
                value={data.branch}
                onChange={handleChange}
                required
              >
                <option value="">Select Branch</option>
                <option value="CAD">CAD</option>
                <option value="CSE">CSE</option>
                <option value="CIVIL">Civil</option>
                <option value="ECE">ECE</option>
                <option value="MECH">Mech</option>
                <option value="EEE">EEE</option>
              </select>
            </div>

            <div className="form-group">
              <label>year</label>

              <select
                name="year"
                value={data.year}
                onChange={(e) => {
                  setData({
                    ...data,
                    [e.target.name]: Number(e.target.value)
                  })
                }}
                required
              >
                <option value="">Select Year</option>
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
              </select>
            </div>
            

            <div className="form-group">
              <select
              name="semister"
              value={data.semister}
              onChange={handleChange}
              required
            >
              <option value="">Select Semester</option>
              <option value="1">1</option>
              <option value="2">2</option>
              <option value="3">3</option>
              <option value="4">4</option>
              <option value="5">5</option>
              <option value="6">6</option>
              <option value="7">7</option>
              <option value="8">8</option>
            </select>
            </div>



            <div className="form-group full-width">
              <label>Password</label>

              <input
                type="password"
                name="password"
                placeholder="Create student password"
                value={data.password}
                onChange={handleChange}
                required
              />
            </div>

          </div>


          <button
            type="submit"
            className="register-btn"
          >
            Add Student
          </button>

        </form>

      </div>

    </div>
  )
}

export default StudentRegister