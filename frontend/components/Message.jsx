export default function Message({ sender, text }) {

    const isUser = sender === "user";

    return (

        <div
            style={{
                display: "flex",
                justifyContent: isUser ? "flex-end" : "flex-start",
                marginBottom: "15px"
            }}
        >

            <div
                style={{
                    background: isUser ? "#2563eb" : "#374151",
                    color: "white",
                    padding: "12px",
                    borderRadius: "10px",
                    maxWidth: "60%"
                }}
            >

                <strong>

                    {isUser ? "👤 You" : "🤖 AI"}

                </strong>

                <br/>

                {text}

            </div>

        </div>

    );

}