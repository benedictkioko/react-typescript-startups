import React,  { useState } from 'react'
import PropTypes from 'prop-types';
import { LazyLoadImage } from 'react-lazy-load-image-component'
import { FaUser, FaLock } from 'react-icons/fa'

export default function Login({ setToken}) {

    const [username, setUserName] = useState();
    const [password, setPassword] = useState();

    return (
        <div className="w-full h-screen flex items-center justify-center">
            <form className="fw-full md:w-1/3 bg-white rounded-lg">
                <div className="flex font-bold justify-center mt-6">
                    <span className="h-20 w-20">
                        <LazyLoadImage src="../../public/avatar.svg" alt=""/>
                    </span>
                </div>
                <h2 class="text-3xl text-center text-gray-700 mb-4 py-5">Sign In</h2>
                <div className="px-12 pb-10">
                    <div className="w-full mb-2">
                        <div className="flex items-center">
                            <FaUser className='ml-3 fill-current text-gray-400 text-xs z-10' />
                            <input type='text' placeholder="Email" className="-mx-6 px-8  w-full border rounded px-3 py-2 text-gray-700 focus:outline-none focus:border-indigo-500" onChange={e => setUserName(e.target.value)} />
                        </div>
                    </div>
                    <div className="w-full mb-2">
                        <div className="flex items-center">
                        <FaLock className='ml-3 fill-current text-gray-400 text-xs z-10'/>
                        <input type='text' placeholder="Password" className="-mx-6 px-8 w-full border rounded px-3 py-2 text-gray-700 focus:outline-none focus:border-indigo-500" onChange={e => setPassword(e.target.value)} />

                        </div>
                    </div>
                   
                    <div className="mt-10">
                        <button className="w-full py-2 rounded-full bg-green-600 text-gray-100 focus:outline-none focus:shodow-outline hover:bg-indigo-600 shadow-lg" type="submit">Login</button>
                    </div>
                </div>
            </form>
        </div>
           
    )
}

Login.propTypes = {
    setToken: PropTypes.func.isRequired
}
