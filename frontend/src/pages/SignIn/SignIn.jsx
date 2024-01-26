import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import './SignIn.css';
const SignIn = () => {
  const [SignIn_MemberData,setSignIn_MemberData] = useState({
    MemberEmail: '',
    MemberPassword: ''
  });
  const navigate = useNavigate();
  const handleChange = (e) => {
    const { name, value } = e.target;
    setSignIn_MemberData({ ...SignIn_MemberData, [name]: value });
  };

  const handleSubmit = async () => {
    console.log(SignIn_MemberData);
    try {
      const response = await axios.post(`http://localhost:8000/api/sign-in/${SignIn_MemberData.MemberEmail}`, {
        Password: SignIn_MemberData.MemberPassword
      });
      console.log(response.data);
      // If response is successful, navigate to inactive page
      navigate('/inactive');
    } catch (error) {
      alert(`Member ${SignIn_MemberData.MemberEmail} isn't exist`)
      // Handle authentication error, display error message to the user
    }
  };

  return (
    <div className="SignIn">
      <div className="SignIn-header">
        <h1>Sign-In</h1>
      </div>
      <div className="SignIn-Field">
        <h4>E-mail</h4>
        <input type='email' placeholder='Email' name='MemberEmail' value={SignIn_MemberData.MemberEmail} onChange={handleChange} />
      </div>
      <div className="SignIn-Field">
        <h4>Password</h4>
        <input type='password' placeholder='password' name='MemberPassword' value={SignIn_MemberData.MemberPassword} onChange={handleChange} />
      </div>
      <div className='SignIn-Button'>
        <div className='SignIn-Submit' onClick={handleSubmit}>
          Sign In
        </div>
      </div>
      <div className='SignIn-move-to-signup'>
        <p>Don't have an account .. 
          <a href='/SignUp'>Sign Up</a>
        </p>
      </div>
    </div>
  )
}

export default SignIn;
