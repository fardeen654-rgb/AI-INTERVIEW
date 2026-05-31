# 🎯 AI Mock Interviewer

An AI-powered mock interview web app that conducts role-specific interviews and gives detailed performance feedback — built with vanilla HTML/CSS/JS and the Claude API.

---

## 🚀 Live Demo

👉 [Click here to try it](https://YourUsername.github.io/YourRepoName)

> Replace the link above with your actual GitHub Pages URL.

---

## ✨ Features

- 🎭 **16+ Job Roles** — Software Engineer, Product Manager, Data Scientist, UI/UX Designer, and more
- 🎯 **Experience Levels** — Fresher, Junior, Mid-level, Senior, Lead/Principal
- 🔀 **Interview Focus** — Technical, Behavioral, System Design, or Mixed
- 🎙️ **Voice + Text Input** — Answer via microphone or type your response
- 🤖 **AI-Generated Questions** — Dynamic questions tailored to your role and level
- 📊 **Detailed Results** — Overall score (out of 10), per-question feedback, strengths and areas to improve
- 🌙 **Dark UI** — Clean, modern dark theme

---

## 🛠️ Tech Stack

| Technology | Usage |
|---|---|
| HTML / CSS / JS | Frontend (no frameworks) |
| Claude API (Sonnet) | AI question generation & feedback |
| Web Speech API | Voice recording & transcription |
| GitHub Pages | Hosting |

---

## 📦 How to Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/YourUsername/YourRepoName.git
cd YourRepoName
```

**2. Start a local server**
```bash
python -m http.server 8000
```

**3. Open in Chrome**
```
http://localhost:8000/index.html
```

> ⚠️ Use Chrome or Edge for voice recording support.

---

## 🔑 API Key

This app uses the [Anthropic Claude API](https://console.anthropic.com/). The API key is handled server-side via the Claude.ai artifact environment.

If you fork this project and want to use your own key, replace the fetch headers in `index.html` with your own `x-api-key`.

---

## 📸 Screenshots

> Add screenshots of your app here after deployment!

---

## 🙌 Author

Made with ❤️ using Claude AI

---

## 📄 License

MIT License — free to use and modify.
