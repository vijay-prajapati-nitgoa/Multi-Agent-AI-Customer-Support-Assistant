export default function Navbar() {

    return (

        <div
            style={{
                height: "60px",
                background: "#1f2937",
                color: "white",
                display: "flex",
                justifyContent: "space-between",
                alignItems: "center",
                padding: "0 20px"
            }}
        >

            <h2>🤖 Multi-Agent AI Customer Support</h2>

            <button
                style={{
                    padding: "8px 15px",
                    cursor: "pointer"
                }}
            >
                Logout
            </button>

        </div>

    );

}