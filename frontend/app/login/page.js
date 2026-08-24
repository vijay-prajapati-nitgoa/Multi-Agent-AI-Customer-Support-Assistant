"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import API from "../../services/api";

export default function Login() {

    const router = useRouter();

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    async function login() {

        try {

            const res = await API.post("/auth/login", {
                email,
                password
            });

            console.log("Login Success:", res.data);

            localStorage.setItem(
                "token",
                res.data.access_token
            );

            alert("Login Successful");

            router.push("/chat");

        } catch (err) {

    console.log("========== LOGIN ERROR ==========");
    console.log(err);

    console.log("Message:", err.message);
    console.log("Code:", err.code);
    console.log("Response:", err.response);
    console.log("Request:", err.request);

    if (err.response) {

        alert(JSON.stringify(err.response.data));

    } else {

        alert(err.message);

    }

}

    }

    return (

        <div
            style={{
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
                height: "100vh",
                backgroundColor: "#0a0a0a"
            }}
        >

            <div
                style={{
                    width: "400px"
                }}
            >

                <h1
                    style={{
                        color: "white",
                        marginBottom: "30px",
                        textAlign: "center"
                    }}
                >
                    Login
                </h1>

                <input
                    type="email"
                    placeholder="Email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    style={{
                        width: "100%",
                        height: "45px",
                        padding: "10px",
                        marginBottom: "20px",
                        border: "1px solid gray",
                        borderRadius: "8px",
                        fontSize: "16px",
                        backgroundColor: "#1f2937",
                        color: "white",
                        outline: "none"
                    }}
                />

                <input
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    style={{
                        width: "100%",
                        height: "45px",
                        padding: "10px",
                        marginBottom: "25px",
                        border: "1px solid gray",
                        borderRadius: "8px",
                        fontSize: "16px",
                        backgroundColor: "#1f2937",
                        color: "white",
                        outline: "none"
                    }}
                />

                <button
                    onClick={login}
                    style={{
                        width: "100%",
                        height: "45px",
                        backgroundColor: "#2563eb",
                        color: "white",
                        border: "none",
                        borderRadius: "8px",
                        fontSize: "18px",
                        cursor: "pointer"
                    }}
                >
                    Login
                </button>

            </div>

        </div>

    );

}