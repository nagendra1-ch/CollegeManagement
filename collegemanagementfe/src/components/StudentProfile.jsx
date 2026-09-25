// import { useState,useEffect } from "react"
// import React from 'react'

// const StudentProfile = () => {
//     const token=localStorage.getItem('access-token')
//     const [details,setDetails]=useState([])
//     const [subjects,setSubjects]=useState([])
//     useEffect(()=>
//         {fetch("http://localhost:8000/api/profile",
//             {
//                 headers: {
//                     Authorization : `Bearer ${token}`
//                 }
//             }
//         ).then((response)=>response.json()).then((data)=>{setDetails(data)
//         }).catch((error)=>console.error(error))},[])

//     useEffect(()=>
//         {fetch("http://127.0.0.1:8000/api/student-marks",
//             {
//                 headers: {
//                     Authorization : `Bearer ${token}`
//                 }
//             }
//         ).then((response)=>response.json()).then((data)=>{setSubjects(data.marks)
            
//         }).catch((error)=>console.error(error))},[token])

//         useEffect(()=>{
//             console.log(subjects)
//         },[subjects])
        
        

//   return (
//     <div>
//         {
//             <div>
//                 <p>First Name : {details.first_name}</p>
//                 <p>Last Name : {details.last_name}</p>
//                 <p>Student ID : {details.Sid}</p>
//                 <p> Email : {details.email}</p>
//                 <p>Department : {details.branch}</p>
//                 <p> Age : {details.age}</p>
//                 <p>Gender : {details.gender}</p>
//                 <p>Phone Number : {details.phone}</p>
//                 <p>Role : {details.role}</p>
//                 <p>Year : {details.year}</p>
//                 <p> Semister : {details.semister}</p>

                
//             </div>

            
//         }

//         <div>
//             {
//                 <p>{subjects.map((subject)=>{
//                     <p> {subject.name} {subject.grade} </p>
//                 })} </p>
//             }
//         </div>

//     </div>
//   )
// }

// export default StudentProfile


import { useState, useEffect } from "react";
import React from "react";
import '../styles/StudentProfile.css'
const StudentProfile = () => {
    const token = localStorage.getItem("access-token");

    const [details, setDetails] = useState([]);
    const [subjects, setSubjects] = useState([]);

    useEffect(() => {
        fetch("http://localhost:8000/api/profile", {
            headers: {
                Authorization: `Bearer ${token}`
            }
        })
            .then((response) => response.json())
            .then((data) => {
                setDetails(data);
            })
            .catch((error) => console.error(error));
    }, []);

    useEffect(() => {
        fetch("http://127.0.0.1:8000/api/student-marks", {
            headers: {
                Authorization: `Bearer ${token}`
            }
        })
            .then((response) => response.json())
            .then((data) => {
                setSubjects(data.marks);
            })
            .catch((error) => console.error(error));
    }, [token]);

    useEffect(() => {
        console.log(subjects);
    }, [subjects]);

    return (
        <div className="student-profile">

            {/* Header */}
            <div className="profile-header">
                <div className="profile-avatar">
                    {details.first_name?.charAt(0)}
                </div>

                <div>
                    <h1>
                        {details.first_name} {details.last_name}
                    </h1>
                    <p>{details.branch}</p>
                </div>
            </div>

            {/* Student Information */}
            <div className="profile-card">
                <div className="card-title">
                    <h2>Student Information</h2>
                </div>

                <div className="details-grid">

                    <div className="detail-item">
                        <span>Student ID</span>
                        <strong>{details.Sid}</strong>
                    </div>

                    <div className="detail-item">
                        <span>Email</span>
                        <strong>{details.email}</strong>
                    </div>

                    <div className="detail-item">
                        <span>Department</span>
                        <strong>{details.branch}</strong>
                    </div>

                    <div className="detail-item">
                        <span>Age</span>
                        <strong>{details.age}</strong>
                    </div>

                    <div className="detail-item">
                        <span>Gender</span>
                        <strong>{details.gender}</strong>
                    </div>

                    <div className="detail-item">
                        <span>Phone Number</span>
                        <strong>{details.phone}</strong>
                    </div>

                    <div className="detail-item">
                        <span>Year</span>
                        <strong>{details.year}</strong>
                    </div>

                    <div className="detail-item">
                        <span>Semester</span>
                        <strong>{details.semister}</strong>
                    </div>

                </div>
            </div>

            {/* Subjects */}
            <div className="subjects-section">

                <div className="section-header">
                    <div>
                        <h2>Academic Performance</h2>
                        <p>Your subjects and grades</p>
                    </div>

                    <div className="subject-count">
                        {subjects.length} Subjects
                    </div>
                </div>

                <div className="subjects-table">

                    <div className="table-header">
                        <div>Subject</div>
                        <div>Code</div>
                        <div>Semester</div>
                        <div>Grade</div>
                    </div>

                    {subjects.map((subject) => (
                        <div className="table-row" key={subject.id}>

                            <div className="subject-name">
                                <div className="subject-icon">
                                    {subject.name.charAt(0)}
                                </div>

                                <div>
                                    <strong>{subject.name}</strong>
                                </div>
                            </div>

                            <div className="subject-code">
                                {subject.code}
                            </div>

                            <div>
                                Semester {subject.semister}
                            </div>

                            <div>
                                <span
                                    className={`grade grade-${subject.grade}`}
                                >
                                    {subject.grade}
                                </span>
                            </div>

                        </div>
                    ))}

                </div>
            </div>

        </div>
    );
};

export default StudentProfile;