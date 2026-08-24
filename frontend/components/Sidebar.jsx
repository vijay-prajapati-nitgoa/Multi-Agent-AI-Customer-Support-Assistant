"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { v4 as uuidv4 } from "uuid";
import API from "../services/api";

export default function Sidebar() {

    const router = useRouter();

    const [sessions, setSessions] = useState([]);

    useEffect(() => {
        loadSessions();
    }, []);

    async function loadSessions() {
        try {
            const res = await API.get("/chat/sessions");
            setSessions(res.data.sessions || []);
        } catch (err) {
            console.log(err);
        }
    }

    function newChat() {

        const id = uuidv4();

        localStorage.setItem("session_id", id);

        window.location.reload();
    }

    function openChat(id) {

        localStorage.setItem("session_id", id);

        window.location.reload();
    }

    async function deleteChat(id) {

        try {

            await API.delete(`/chat/${id}`);

            const current = localStorage.getItem("session_id");

            if (current === id) {

                localStorage.removeItem("session_id");

            }

            loadSessions();

        }

        catch (err) {

            console.log(err);

        }

    }

    return (

        <div
            style={{
                width: "270px",
                background: "#111827",
                color: "white",
                height: "100vh",
                padding: "20px",
                borderRight: "1px solid #374151",
                overflowY: "auto",
                boxSizing: "border-box"
            }}
        >

            <h2
                style={{
                    marginBottom: "20px"
                }}
            >
                Chats
            </h2>

            {/* New Chat */}

            <button

                onClick={newChat}

                style={{
                    width: "100%",
                    padding: "12px",
                    marginBottom: "10px",
                    background: "#2563EB",
                    border: "none",
                    color: "white",
                    borderRadius: "8px",
                    cursor: "pointer",
                    fontSize: "15px",
                    fontWeight: "bold"
                }}

            >

                + New Chat

            </button>

            {/* Upload PDF */}

            <button

                onClick={() => router.push("/upload")}

                style={{
                    width: "100%",
                    padding: "12px",
                    marginBottom: "20px",
                    background: "#10B981",
                    border: "none",
                    color: "white",
                    borderRadius: "8px",
                    cursor: "pointer",
                    fontSize: "15px",
                    fontWeight: "bold"
                }}

            >

                📄 Upload PDF

            </button>

            <hr
                style={{
                    border: "1px solid #374151",
                    marginBottom: "20px"
                }}
            />

            <h3
                style={{
                    marginBottom: "15px"
                }}
            >
                Chat History
            </h3>

            {

                sessions.length === 0 ?

                (

                    <p
                        style={{
                            color: "#9CA3AF"
                        }}
                    >
                        No chats available
                    </p>

                )

                :

                sessions.map((id, index) => (

                    <div

                        key={id}

                        style={{
                            background: "#1F2937",
                            borderRadius: "8px",
                            padding: "12px",
                            marginBottom: "12px"
                        }}

                    >

                        <div

                            onClick={() => openChat(id)}

                            style={{
                                cursor: "pointer",
                                fontWeight: "bold",
                                marginBottom: "8px"
                            }}

                        >

                            💬 Chat {index + 1}

                        </div>

                        <div

                            style={{
                                fontSize: "11px",
                                color: "#9CA3AF",
                                wordBreak: "break-all",
                                marginBottom: "10px"
                            }}

                        >

                            {id}

                        </div>

                        <button

                            onClick={() => deleteChat(id)}

                            style={{
                                width: "100%",
                                background: "#DC2626",
                                color: "white",
                                border: "none",
                                padding: "8px",
                                borderRadius: "6px",
                                cursor: "pointer"
                            }}

                        >

                            Delete

                        </button>

                    </div>

                ))

            }

        </div>

    );

}