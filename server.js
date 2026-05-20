import express from "express";
import fetch from "node-fetch";

const app = express();
app.use(express.json());

// 🔑 ТВОИ ДАННЫЕ
const TOKEN = "YOUR_GITHUB_TOKEN";
const REPO = "nikita_47475";

app.post("/publish", async (req, res) => {
  const { ip, device } = req.body;

  const filename = `db/${Date.now()}.json`;

  const content = Buffer.from(JSON.stringify({
    ip,
    device,
    time: new Date().toISOString()
  })).toString("base64");

  const github = await fetch(
    `https://api.github.com/repos/${REPO}/contents/${filename}`,
    {
      method: "PUT",
      headers: {
        Authorization: `Bearer ${TOKEN}`,
        Accept: "application/vnd.github+json"
      },
      body: JSON.stringify({
        message: "IP log",
        content
      })
    }
  );

  const data = await github.json();

  res.json({ ok: true, file: filename });
});

app.listen(3000, () => {
  console.log("Server running on http://localhost:3000");
});
