import type React from "react";
import { useState } from "react";

const HappyApp: React.FC = () => {
	const [message, setMessage] = useState<string>("こんにちは！");

	const getCurrentTimeString = (): string => {
		const now = new Date();
		return now.toLocaleString("ja-JP");
	};

	const handleHeartClick = (): void => {
		setMessage("幸せが届きました！");
	};

	return (
		<div
			style={{
				textAlign: "center",
				padding: "2rem",
				fontFamily: "Arial, sans-serif",
			}}
		>
			<h1 style={{ color: "#ff69b4" }}>💗 makeHappy</h1>
			<p style={{ fontSize: "1.2rem", color: "#333" }}>{message}</p>
			<p style={{ fontSize: "0.9rem", color: "#999" }}>
				現在の日時: {getCurrentTimeString()}
			</p>
			<button
				type="button"
				onClick={handleHeartClick}
				style={{
					fontSize: "3rem",
					background: "none",
					border: "none",
					cursor: "pointer",
					padding: "1rem",
					transition: "transform 0.2s",
				}}
				onMouseEnter={(e) => {
					e.currentTarget.style.transform = "scale(1.2)";
				}}
				onMouseLeave={(e) => {
					e.currentTarget.style.transform = "scale(1)";
				}}
			>
				❤️
			</button>
		</div>
	);
};

export default HappyApp;
