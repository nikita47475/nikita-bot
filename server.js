import express from "express";
import fetch from "node-fetch";

const app = express();
app.use(express.json());

const TOKEN = "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";
const REPO = "nikita47475
";

app.post("/publish", async (req, res) => {
  const { ip, device } = req.body;

  const filename = `db/${Date.now()}.json`;

  const content = Buffer.from(JSON.stringify({
    ip,
    device,
    time: new Date().toISOString()
  })).toString("base64");

  try {
    const response = await fetch(
      `https://api.github.com/repos/${REPO}/contents/${filename}`,
      {
        method: "PUT",
        headers: {
          Authorization: `Bearer ${TOKEN}`,
          Accept: "application/vnd.github+json"
        },
        body: JSON.stringify({
          message: "IP запись",
          content
        })
      }
    );

    const data = await response.json();
    res.json({ ok: true });
  } catch (e) {
    res.status(500).json({ ok: false });
  }
});

app.listen(3000, () => {
  console.log("Сервер запущен: http://localhost:3000");
});
