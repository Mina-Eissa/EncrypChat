import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import './SignUp.css';
const SignUp = () => {
    const [SignUp_MemberData, setSignUp_MemberData] = useState({
        MemberName: '',
        MemberEmail: '',
        MemberPhoneNumber: '',
        MemberPassword: '',
        MemberConfirmPassword: '',
        MemberBirthDate:''
    });
    const navigate = useNavigate();
    const handleChange = (e) => {
        const { name, value } = e.target;
        setSignUp_MemberData({ ...SignUp_MemberData, [name]: value });
    };
    
    const handleSubmit = async () => {
        if (SignUp_MemberData.MemberPassword !== SignUp_MemberData.MemberConfirmPassword) {
            alert("Password don't match confirmed password");
            return
        }
        console.log(SignUp_MemberData);
        try {
            const response = await axios.post(`http://localhost:8000/api/sign-up/`, {
                Name: SignUp_MemberData.MemberName,
                Email: SignUp_MemberData.MemberEmail,
                PhoneNumber: SignUp_MemberData.MemberPhoneNumber,
                Password: SignUp_MemberData.MemberPassword,
                BirthDate:SignUp_MemberData.MemberBirthDate
            });
            console.log(response.status)
            alert(`Member ${SignUp_MemberData.MemberName} is successfully created`);
            // If response is successful, navigate to inactive page
            navigate('/inactive');
        } catch (error) {
            alert(`Member ${SignUp_MemberData.MemberEmail} doesn't signed up`);
            // Handle authentication error, display error message to the user
        }
    };
    return (
        <div className="SignUp">
            <div className="SignUp-header">
                <h1>Sign-Up</h1>
            </div>
            <div className="SignUp-Field">
                <h4>User Name</h4>
                <input type='text' placeholder='username' name='MemberName' value={SignUp_MemberData.MemberName} onChange={handleChange} />
            </div>
            <div className="SignUp-Field">
                <h4>E-mail</h4>
                <input type='email' placeholder='example@example.com' name='MemberEmail' value={SignUp_MemberData.MemberEmail} onChange={handleChange} />
            </div>
            <div className='SignUp-double-division'>
                <div className="SignUp-Field">
                    <h4>Phone Number</h4>
                    <input type='text' placeholder='ex:01012345678' name='MemberPhoneNumber' value={SignUp_MemberData.MemberPhoneNumber} onChange={handleChange} />
                </div>
                <div className="SignUp-Field">
                    <h4>Birth Date</h4>
                    <input type='text' placeholder='2001-01-01' name='MemberBirthDate' value={SignUp_MemberData.MemberBirthDate} onChange={handleChange} />
                </div>
            </div>
            <div className='SignUp-double-division'>
                <div className="SignUp-Field">
                    <h4>Password</h4>
                    <input type='password' placeholder='password' name='MemberPassword' value={SignUp_MemberData.MemberPassword} onChange={handleChange} />
                </div>
                <div className="SignUp-Field">
                    <h4>Confirm Password</h4>
                    <input type='password' placeholder='re-enter password' name='MemberConfirmPassword' value={SignUp_MemberData.MemberConfirmPassword} onChange={handleChange} />
                </div>
            </div>
            <div className='SignUp-Button'>
                <div className='SignUp-Submit' onClick={handleSubmit}>
                    Sign Up
                </div>
            </div>
        </div>
    )
}
export default SignUp;