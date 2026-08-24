"use client";

import { useState } from "react";
import API from "../services/api";

export default function Upload() {

    const [file, setFile] = useState(null);
    const [loading, setLoading] = useState(false);

    async function uploadPDF() {

        if (!file) {
            alert("Please select a PDF file.");
            return;
        }

        const formData = new FormData();
        formData.append("file", file);

        setLoading(true);

        try {

            const res = await API.post(
                "/upload",
                formData,
                {
                    headers: {
                        "Content-Type": "multipart/form-data"
                    }
                }
            );

            alert(res.data.message || "PDF uploaded successfully!");

            setFile(null);

        }
        catch (err) {

            console.log(err);

            alert("Failed to upload PDF.");

        }

        setLoading(false);

    }

    return (

        <div
            style={{
                minHeight: "100vh",
                background: "#0a0a0a",
                color: "white",
                display: "flex",
                justifyContent: "center",
                alignItems: "center"
            }}
        >

            <div
                style={{
                    width: "450px",
                    background: "#1F2937",
                    padding: "30px",
                    borderRadius: "12px"
                }}
            >

                <h2
                    style={{
                        textAlign: "center",
                        marginBottom: "25px"
                    }}
                >
                    Upload PDF
                </h2>

                <input
                    type="file"
                    accept=".pdf"
                    onChange={(e) => setFile(e.target.files[0])}
                    style={{
                        width: "100%",
                        marginBottom: "20px"
                    }}
                />

                {file && (

                    <p
                        style={{
                            color: "#9CA3AF",
                            marginBottom: "20px"
                        }}
                    >
                        Selected File: <strong>{file.name}</strong>
                    </p>

                )}

                <button

                    onClick={uploadPDF}

                    disabled={loading}

                    style={{
                        width: "100%",
                        padding: "12px",
                        background: loading ? "#6B7280" : "#2563EB",
                        color: "white",
                        border: "none",
                        borderRadius: "8px",
                        cursor: loading ? "not-allowed" : "pointer",
                        fontSize: "16px"
                    }}

                >

                    {loading ? "Uploading..." : "Upload PDF"}

                </button>

            </div>

        </div>

    );

}