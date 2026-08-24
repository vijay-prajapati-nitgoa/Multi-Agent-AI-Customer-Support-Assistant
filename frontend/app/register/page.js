"use client";

import { useState } from "react";
import API from "../../services/api";
import { useRouter } from "next/navigation";

export default function Register() {

    const router = useRouter();

    const [name,setName]=useState("");

    const [email,setEmail]=useState("");

    const [password,setPassword]=useState("");

    async function register(){

        try{

            await API.post("/auth/register",{

                name,

                email,

                password

            });

            alert("Registration Successful");

            router.push("/login");

        }

        catch{

            alert("Registration Failed");

        }

    }

    return(

        <div style={{padding:40}}>

            <h1>Register</h1>

            <input

                placeholder="Name"

                value={name}

                onChange={(e)=>setName(e.target.value)}

            />

            <br/><br/>

            <input

                placeholder="Email"

                value={email}

                onChange={(e)=>setEmail(e.target.value)}

            />

            <br/><br/>

            <input

                type="password"

                placeholder="Password"

                value={password}

                onChange={(e)=>setPassword(e.target.value)}

            />

            <br/><br/>

            <button onClick={register}>

                Register

            </button>

        </div>

    );

}