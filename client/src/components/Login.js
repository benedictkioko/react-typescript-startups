import React from 'react'

export default function Login() {
    return (
        <div className="mt-10 px-12 sm:px-24 md:px-48 lg:px-12 lg:mt-16 xl:px-24 xl:max-w-2xl">
                <h1 className="text-center text=4xl test-indigo-900 font-display font-semibold lg:text-center xl:text-5xl">Log In</h1>
                <div mt-12>
                    <form>
                        <label>
                            <div className="text-lg font-bold text-gray-700 tracking-wide">Email</div>
                            <input className="w-full text-lg py-2 border-gray-300 focus:outline-none focus:border-indigo-500" type="text" placeholder="mail@startups.com"/>
                        </label>
                        <label>
                            <div className="text-lg font-bold text-gray-700 tracking-wide">Password</div>
                            <input className="w-full text-lg py-2 border-gray-300 focus:outline-none focus:border-indigo-500" type="password" placeholder="Enter your Password" />
                        </label>
                        <div className="mt-10">
                            <button className="bg-indigo-500 text-gray-100 p-4 w-full rounded-full tracking-wide font-semibold font-display focus:outline-none focus:shodow-outline hover:bg-indigo-600 shadow-lg" type="submit">Login</button>
                        </div>
                    </form>
                </div>
        </div>
    )
}
