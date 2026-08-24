import { useState } from "react";

const API = "http://127.0.0.1:8000";

export default function App() {

  const [email, setEmail] = useState(
    "analyst@example.com"
  );

  const [password, setPassword] = useState(
    "ChangeMe-Analyst-123!"
  );

  const [prompt, setPrompt] = useState("");

  const [token, setToken] = useState("");

  const [answer, setAnswer] = useState("");

  const [loading, setLoading] = useState(false);

  async function login() {

    const response = await fetch(
      `${API}/api/v1/auth/login`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          email,
          password
        })
      }
    );

    if (!response.ok) {
      throw new Error("Authentication failed");
    }

    const data = await response.json();

    setToken(data.access_token);
  }

  async function sendMessage() {

    if (!token) {
      await login();
      return;
    }

    setLoading(true);

    try {

      const response = await fetch(
        `${API}/api/v1/agent/chat`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`
          },
          body: JSON.stringify({
            prompt
          })
        }
      );

      const data = await response.json();

      setAnswer(
        response.ok
          ? data.answer
          : `Blocked: ${data.detail}`
      );

    } finally {

      setLoading(false);
    }
  }

  return (
    <main className="container">

      <h1>Secure Agent</h1>

      <p>
        Enterprise AI Agent Security Lab
      </p>

      {!token && (
        <section>

          <input
            value={email}
            onChange={(e) =>
              setEmail(e.target.value)
            }
            placeholder="Email"
          />

          <input
            type="password"
            value={password}
            onChange={(e) =>
              setPassword(e.target.value)
            }
            placeholder="Password"
          />

          <button onClick={login}>
            Authenticate
          </button>

        </section>
      )}

      <section>

        <textarea
          value={prompt}
          onChange={(e) =>
            setPrompt(e.target.value)
          }
          placeholder="Ask Secure Agent..."
        />

        <button
          onClick={sendMessage}
          disabled={loading}
        >
          {loading ? "Processing..." : "Send"}
        </button>

      </section>

      <section className="response">

        <h2>Agent Response</h2>

        <pre>
          {answer}
        </pre>

      </section>

    </main>
  );
}