import type React from "react";
import { useState } from "react";

const HappyApp: React.FC = () => {
	const [message, setMessage] = useState("");

	const handleClick = () => {
		setMessage("幸せが届きました！");
	};

	return (
		<div style={{ textAlign: "center", marginTop: "50px" }}>
			<h1>こんにちは！</h1>
			<p>現在の日時: {new Date().toLocaleString()}</p>
			<button onClick={handleClick} style={{ fontSize: "24px", padding: "10px 20px" }}>
				❤️
			</button>
			{message && <p style={{ marginTop: "20px", fontSize: "18px" }}>{message}</p>}
		</div>
	);
};

export default HappyApp;
