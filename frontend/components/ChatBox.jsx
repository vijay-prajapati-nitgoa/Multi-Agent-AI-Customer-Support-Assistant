"use client";

import { useEffect, useState } from "react";
import { v4 as uuidv4 } from "uuid";
import API from "../services/api";

export default function ChatBox() {

    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState("");
    const [loading, setLoading] = useState(false);

    // =========================================
    // SESSION
    // =========================================

    useEffect(() => {

        let sessionId =
            localStorage.getItem("session_id");

        if (!sessionId) {

            sessionId = uuidv4();

            localStorage.setItem(
                "session_id",
                sessionId
            );
        }

        loadChat(sessionId);

    }, []);


    // =========================================
    // FORMAT CONTENT
    // =========================================

    function formatContent(content) {

        if (
            content === null ||
            content === undefined
        ) {
            return "";
        }


        // STRING
        if (typeof content === "string") {

            // Check for character-by-character
            // response:
            //
            // C
            // u
            // s
            // t
            // o
            // m
            // e
            // r
            //
            // We keep spaces if they exist.

            const rawLines =
                content.split(/\r?\n/);

            const nonEmptyLines =
                rawLines.filter(
                    line => line.length > 0
                );

            if (
                nonEmptyLines.length > 5 &&
                nonEmptyLines.every(
                    line =>
                        line.length === 1
                )
            ) {

                return nonEmptyLines.join("");
            }

            return content;
        }


        // ARRAY
        if (Array.isArray(content)) {

            if (
                content.every(
                    item =>
                        typeof item === "string"
                )
            ) {

                return content.join("");
            }

            return content
                .map(item => {

                    if (
                        typeof item === "string"
                    ) {
                        return item;
                    }

                    if (
                        typeof item === "object" &&
                        item !== null &&
                        "text" in item
                    ) {
                        return String(
                            item.text
                        );
                    }

                    return "";

                })
                .join("");
        }


        // OBJECT
        if (
            typeof content === "object"
        ) {

            if (
                content.response !== undefined
            ) {

                return formatContent(
                    content.response
                );
            }

            if (
                content.content !== undefined
            ) {

                return formatContent(
                    content.content
                );
            }

            return JSON.stringify(
                content,
                null,
                2
            );
        }


        return String(content);
    }


    // =========================================
    // LOAD CHAT
    // =========================================

    async function loadChat(sessionId) {

        try {

            const res =
                await API.get(
                    `/chat/${sessionId}`
                );

            console.log(
                "Chat history:",
                res.data
            );

            if (
                res.data &&
                Array.isArray(
                    res.data.messages
                )
            ) {

                const formattedMessages =
                    res.data.messages.map(
                        msg => ({
                            role: msg.role,
                            content:
                                formatContent(
                                    msg.content
                                )
                        })
                    );

                setMessages(
                    formattedMessages
                );
            }

        } catch (err) {

            console.log(
                "Could not load chat history:",
                err
            );
        }
    }


    // =========================================
    // SEND MESSAGE
    // =========================================

    async function sendMessage() {

        const message =
            input.trim();

        if (
            !message ||
            loading
        ) {
            return;
        }

        let sessionId =
            localStorage.getItem(
                "session_id"
            );

        if (!sessionId) {

            sessionId = uuidv4();

            localStorage.setItem(
                "session_id",
                sessionId
            );
        }


        // User message

        setMessages(prev => [
            ...prev,
            {
                role: "user",
                content: message
            }
        ]);

        setInput("");
        setLoading(true);


        try {

            console.log(
                "Sending message:",
                message
            );

            const res =
                await API.post(
                    "/chat",
                    {
                        session_id:
                            sessionId,

                        query:
                            message
                    }
                );


            console.log(
                "Backend response:",
                res.data
            );


            console.log(
                "Response:",
                JSON.stringify(
                    res.data.response
                )
            );


            const answer =
                formatContent(
                    res.data
                );


            setMessages(prev => [
                ...prev,
                {
                    role: "assistant",
                    content: answer
                }
            ]);

        } catch (err) {

            console.error(
                "Chat error:",
                err
            );

            setMessages(prev => [
                ...prev,
                {
                    role: "assistant",
                    content:
                        "Unable to connect to backend."
                }
            ]);

        } finally {

            setLoading(false);
        }
    }


    // =========================================
    // ENTER KEY
    // =========================================

    function handleKeyDown(e) {

        if (
            e.key === "Enter" &&
            !e.shiftKey
        ) {

            e.preventDefault();

            sendMessage();
        }
    }


    // =========================================
    // UI
    // =========================================

    return (

        <div
            style={{
                display: "flex",
                flexDirection: "column",

                /*
                 * IMPORTANT:
                 * Allows ChatBox to stay
                 * inside available width.
                 */
                flex: 1,
                minWidth: 0,
                width: "100%",

                height: "100vh",

                background: "#0B0F19",
                color: "white",

                boxSizing: "border-box"
            }}
        >


            {/* =================================
                MESSAGES
            ================================= */}

            <div
                style={{
                    flex: 1,

                    minWidth: 0,

                    width: "100%",

                    overflowY: "auto",
                    overflowX: "hidden",

                    padding: "30px",

                    boxSizing: "border-box"
                }}
            >

                {messages.length === 0 && (

                    <div
                        style={{
                            textAlign: "center",

                            color: "#9CA3AF",

                            marginTop: "100px",

                            fontSize: "20px"
                        }}
                    >
                        Start a new conversation
                    </div>
                )}


                {messages.map(
                    (msg, index) => {

                        const isUser =
                            msg.role === "user";


                        return (

                            <div
                                key={index}

                                style={{
                                    display: "flex",

                                    justifyContent:
                                        isUser
                                            ? "flex-end"
                                            : "flex-start",

                                    width: "100%",

                                    minWidth: 0,

                                    marginBottom: "20px"
                                }}
                            >

                                <div
                                    style={{
                                        /*
                                         * IMPORTANT:
                                         * Don't let the
                                         * message push
                                         * the whole page.
                                         */
                                        maxWidth: "75%",

                                        minWidth: "0",

                                        padding:
                                            "15px 18px",

                                        borderRadius:
                                            "12px",

                                        background:
                                            isUser
                                                ? "#2563EB"
                                                : "#374151",

                                        color: "white",

                                        fontSize: "17px",

                                        lineHeight: "1.5",

                                        whiteSpace:
                                            "pre-wrap",

                                        overflowWrap:
                                            "anywhere",

                                        wordBreak:
                                            "normal",

                                        boxSizing:
                                            "border-box"
                                    }}
                                >

                                    {/* NAME */}

                                    <div
                                        style={{
                                            fontWeight:
                                                "bold",

                                            marginBottom:
                                                "8px"
                                        }}
                                    >

                                        {isUser
                                            ? "👤 You"
                                            : "🤖 AI"}

                                    </div>


                                    {/* MESSAGE */}

                                    <div
                                        style={{
                                            whiteSpace:
                                                "pre-wrap",

                                            overflowWrap:
                                                "anywhere",

                                            wordBreak:
                                                "normal"
                                        }}
                                    >

                                        {formatContent(
                                            msg.content
                                        )}

                                    </div>

                                </div>

                            </div>
                        );
                    }
                )}


                {/* LOADING */}

                {loading && (

                    <div
                        style={{
                            display: "flex",

                            justifyContent:
                                "flex-start",

                            marginBottom:
                                "20px"
                        }}
                    >

                        <div
                            style={{
                                background:
                                    "#374151",

                                padding:
                                    "15px 18px",

                                borderRadius:
                                    "12px",

                                color:
                                    "#D1D5DB"
                            }}
                        >

                            🤖 AI is thinking...

                        </div>

                    </div>
                )}

            </div>


            {/* =================================
                INPUT
            ================================= */}

            <div
                style={{
                    display: "flex",

                    gap: "12px",

                    padding:
                        "15px 20px",

                    borderTop:
                        "1px solid #374151",

                    background:
                        "#111827",

                    width: "100%",

                    boxSizing: "border-box"
                }}
            >

                <textarea

                    value={input}

                    onChange={(e) =>
                        setInput(
                            e.target.value
                        )
                    }

                    onKeyDown={
                        handleKeyDown
                    }

                    placeholder=
                        "Ask your question..."

                    rows={1}

                    disabled={loading}

                    style={{
                        flex: 1,

                        minWidth: 0,

                        resize: "none",

                        padding: "15px",

                        borderRadius:
                            "10px",

                        border:
                            "1px solid #4B5563",

                        background:
                            "#1F2937",

                        color: "white",

                        fontSize: "17px",

                        outline: "none",

                        boxSizing:
                            "border-box"
                    }}
                />


                {/* SEND */}

                <button

                    onClick={
                        sendMessage
                    }

                    disabled={
                        loading ||
                        !input.trim()
                    }

                    style={{
                        flexShrink: 0,

                        width: "120px",

                        border: "none",

                        borderRadius:
                            "10px",

                        background:
                            loading ||
                            !input.trim()
                                ? "#4B5563"
                                : "#2563EB",

                        color: "white",

                        fontSize: "17px",

                        fontWeight:
                            "bold",

                        cursor:
                            loading ||
                            !input.trim()
                                ? "not-allowed"
                                : "pointer"
                    }}
                >

                    {loading
                        ? "..."
                        : "Send"}

                </button>

            </div>

        </div>
    );
}