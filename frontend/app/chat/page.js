"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";

import Navbar from "../../components/Navbar";
import Sidebar from "../../components/Sidebar";
import ChatBox from "../../components/ChatBox";

export default function ChatPage() {

    const router = useRouter();

    useEffect(() => {

        const token = localStorage.getItem("token");

        if (!token) {
            router.push("/login");
        }

    }, [router]);

    return (
        <div>
            <Navbar />

            <div style={{ display: "flex" }}>
                <Sidebar />
                <ChatBox />
            </div>
        </div>
    );
}