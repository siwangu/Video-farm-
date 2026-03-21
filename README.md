<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Video Farm — README</title>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;700&family=Syne:wght@400;700;800&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #0a0a0f;
    --surface: #111118;
    --border: #1e1e2e;
    --accent: #00ff88;
    --accent2: #ff4d6d;
    --accent3: #7c6aff;
    --text: #e2e2f0;
    --muted: #5a5a7a;
    --code-bg: #0d0d17;
    --glow: 0 0 20px rgba(0, 255, 136, 0.15);
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    font-family: 'JetBrains Mono', monospace;
    background: var(--bg);
    color: var(--text);
    line-height: 1.7;
    min-height: 100vh;
  }

  /* Grid background */
  body::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
      linear-gradient(rgba(124, 106, 255, 0.04) 1px, transparent 1px),
      linear-gradient(90deg, rgba(124, 106, 255, 0.04) 1px, transparent 1px);
    background-size: 40px 40px;
    pointer-events: none;
    z-index: 0;
  }

  .container {
    max-width: 860px;
    margin: 0 auto;
    padding: 60px 32px 120px;
    position: relative;
    z-index: 1;
  }

  /* HEADER */
  .header {
    border-bottom: 1px solid var(--border);
    padding-bottom: 48px;
    margin-bottom: 56px;
    position: relative;
  }

  .header::after {
    content: '';
    position: absolute;
    bottom: -1px;
    left: 0;
    width: 120px;
    height: 1px;
    background: var(--accent);
    box-shadow: var(--glow);
  }

  .badge-row {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    margin-bottom: 28px;
    animation: fadeUp 0.6s ease both;
  }

  .badge {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    padding: 4px 10px;
    border-radius: 3px;
    border: 1px solid;
  }

  .badge-green { border-color: var(--accent); color: var(--accent); background: rgba(0,255,136,0.06); }
  .badge-red   { border-color: var(--accent2); color: var(--accent2); background: rgba(255,77,109,0.06); }
  .badge-purple{ border-color: var(--accent3); color: var(--accent3); background: rgba(124,106,255,0.06); }

  h1 {
    font-family: 'Syne', sans-serif;
    font-size: clamp(42px, 8vw, 72px);
    font-weight: 800;
    line-height: 1;
    letter-spacing: -0.03em;
    animation: fadeUp 0.6s 0.1s ease both;
  }

  h1 span {
    color: var(--accent);
    text-shadow: 0 0 30px rgba(0,255,136,0.4);
  }

  .tagline {
    margin-top: 16px;
    color: var(--muted);
    font-size: 13px;
    letter-spacing: 0.04em;
    animation: fadeUp 0.6s 0.2s ease both;
  }

  /* SECTIONS */
  section {
    margin-bottom: 56px;
    animation: fadeUp 0.6s 0.3s ease both;
  }

  h2 {
    font-family: 'Syne', sans-serif;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 10px;
  }

  h2::after {
    content: '';
    flex: 1;
    height: 1px;
    background: var(--border);
    max-width: 200px;
  }

  h3 {
    font-family: 'Syne', sans-serif;
    font-size: 18px;
    font-weight: 700;
    color: var(--text);
    margin-bottom: 12px;
    margin-top: 28px;
  }

  p {
    color: #9898b8;
    font-size: 13px;
    margin-bottom: 14px;
    line-height: 1.8;
  }

  /* INTRO BLOCK */
  .intro-box {
    background: var(--surface);
    border: 1px solid var(--border);
    border-left: 3px solid var(--accent3);
    padding: 24px 28px;
    border-radius: 4px;
    font-size: 13px;
    color: #9898b8;
    line-height: 1.9;
  }

  /* FEATURE GRID */
  .feature-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(230px, 1fr));
    gap: 1px;
    background: var(--border);
    border: 1px solid var(--border);
    border-radius: 6px;
    overflow: hidden;
  }

  .feature-item {
    background: var(--surface);
    padding: 20px 22px;
    transition: background 0.2s;
  }

  .feature-item:hover { background: #161622; }

  .feature-icon {
    font-size: 18px;
    margin-bottom: 10px;
    display: block;
  }

  .feature-title {
    font-size: 12px;
    font-weight: 700;
    color: var(--text);
    letter-spacing: 0.04em;
    margin-bottom: 4px;
  }

  .feature-desc {
    font-size: 11px;
    color: var(--muted);
    line-height: 1.6;
  }

  /* STRUCTURE TREE */
  .tree {
    background: var(--code-bg);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 28px 32px;
    font-size: 13px;
    line-height: 2;
    overflow-x: auto;
  }

  .tree-root { color: var(--accent); font-weight: 700; }
  .tree-dir  { color: var(--accent3); }
  .tree-file { color: #9898b8; }
  .tree-line { color: var(--border); }
  .tree-desc { color: var(--muted); font-size: 11px; margin-left: 8px; }

  /* CODE BLOCKS */
  pre {
    background: var(--code-bg);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 20px 24px;
    overflow-x: auto;
    font-size: 12px;
    line-height: 1.8;
    position: relative;
    margin: 14px 0;
  }

  pre::before {
    content: attr(data-lang);
    position: absolute;
    top: 10px;
    right: 14px;
    font-size: 10px;
    color: var(--muted);
    letter-spacing: 0.1em;
    text-transform: uppercase;
  }

  code { color: var(--accent); }
  .cmd { color: #7c6aff; }
  .str { color: #ff9f70; }
  .cm  { color: var(--muted); }
  .kw  { color: #ff4d6d; }

  /* FILE TABLE */
  .file-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 12px;
    border: 1px solid var(--border);
    border-radius: 6px;
    overflow: hidden;
  }

  .file-table th {
    background: #111120;
    padding: 12px 18px;
    text-align: left;
    font-size: 10px;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--muted);
    border-bottom: 1px solid var(--border);
  }

  .file-table td {
    padding: 12px 18px;
    border-bottom: 1px solid var(--border);
    color: #9898b8;
    vertical-align: top;
  }

  .file-table tr:last-child td { border-bottom: none; }
  .file-table tr:hover td { background: rgba(124,106,255,0.03); }

  .file-name {
    font-weight: 500;
    color: var(--accent3);
    white-space: nowrap;
  }

  /* STEPS */
  .steps { display: flex; flex-direction: column; gap: 2px; }

  .step {
    display: flex;
    gap: 20px;
    align-items: flex-start;
    position: relative;
  }

  .step-num {
    width: 28px;
    height: 28px;
    border: 1px solid var(--accent);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 11px;
    color: var(--accent);
    font-weight: 700;
    flex-shrink: 0;
    margin-top: 2px;
  }

  .step-content { flex: 1; padding-bottom: 28px; }
  .step-title { font-size: 14px; font-weight: 700; color: var(--text); margin-bottom: 8px; }

  /* FLOW DIAGRAM */
  .flow {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 0;
    padding: 28px;
    background: var(--code-bg);
    border: 1px solid var(--border);
    border-radius: 6px;
  }

  .flow-step {
    display: flex;
    align-items: center;
    gap: 14px;
    padding: 10px 16px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 4px;
    font-size: 12px;
    width: 100%;
    transition: border-color 0.2s;
  }

  .flow-step:hover { border-color: var(--accent3); }
  .flow-arrow {
    color: var(--muted);
    font-size: 16px;
    padding: 4px 0 4px 22px;
  }

  .flow-icon { font-size: 16px; }
  .flow-label { color: var(--text); font-weight: 500; }
  .flow-sub { color: var(--muted); font-size: 11px; margin-left: auto; }

  /* ROTATION TABLE */
  .rotation {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1px;
    background: var(--border);
    border: 1px solid var(--border);
    border-radius: 6px;
    overflow: hidden;
    font-size: 12px;
  }

  .rot-cell {
    background: var(--surface);
    padding: 14px 18px;
    text-align: center;
  }

  .rot-cell.header {
    background: #111120;
    color: var(--muted);
    font-size: 10px;
    letter-spacing: 0.12em;
    text-transform: uppercase;
  }

  .rot-video { color: #9898b8; }
  .rot-acc1 { color: var(--accent); font-weight: 600; }
  .rot-acc2 { color: var(--accent3); font-weight: 600; }

  /* LOG BLOCK */
  .log {
    background: var(--code-bg);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 20px 24px;
    font-size: 12px;
    line-height: 2;
  }

  .log-info { color: var(--accent); }
  .log-time { color: var(--muted); }
  .log-msg  { color: #9898b8; }

  /* NOTES */
  .note-list { list-style: none; display: flex; flex-direction: column; gap: 10px; }

  .note-list li {
    display: flex;
    gap: 12px;
    align-items: flex-start;
    font-size: 12px;
    color: #9898b8;
    background: var(--surface);
    border: 1px solid var(--border);
    padding: 12px 16px;
    border-radius: 4px;
  }

  .note-list li::before {
    content: '⚠';
    color: #ffcc5c;
    flex-shrink: 0;
    margin-top: 1px;
  }

  /* LICENSE */
  .license-box {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 24px 28px;
    display: flex;
    align-items: center;
    gap: 20px;
  }

  .license-badge {
    font-family: 'Syne', sans-serif;
    font-size: 22px;
    font-weight: 800;
    color: var(--accent);
    white-space: nowrap;
  }

  .license-desc { font-size: 12px; color: var(--muted); line-height: 1.8; }

  /* FOOTER */
  footer {
    margin-top: 80px;
    padding-top: 24px;
    border-top: 1px solid var(--border);
    font-size: 11px;
    color: var(--muted);
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 8px;
  }

  .footer-accent { color: var(--accent); }

  /* ANIMATIONS */
  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(16px); }
    to   { opacity: 1; transform: translateY(0); }
  }

  section { animation: fadeUp 0.6s ease both; }
  section:nth-child(2) { animation-delay: 0.1s; }
  section:nth-child(3) { animation-delay: 0.15s; }
  section:nth-child(4) { animation-delay: 0.2s; }
  section:nth-child(5) { animation-delay: 0.25s; }
  section:nth-child(6) { animation-delay: 0.3s; }
  section:nth-child(7) { animation-delay: 0.35s; }

  /* INLINE CODE */
  .ic {
    background: rgba(124,106,255,0.12);
    color: var(--accent3);
    padding: 1px 6px;
    border-radius: 3px;
    font-size: 12px;
  }

  a { color: var(--accent3); text-decoration: none; }
  a:hover { text-decoration: underline; }
</style>
</head>
<body>

<div class="container">

  <!-- HEADER -->
  <header class="header">
    <div class="badge-row">
      <span class="badge badge-green">Python 3.9+</span>
      <span class="badge badge-purple">YouTube API v3</span>
      <span class="badge badge-red">MIT License</span>
      <span class="badge badge-green">Termux / Linux / macOS</span>
    </div>
    <h1>Video<span>Farm</span></h1>
    <p class="tagline">// Automated video generation &amp; multi-channel YouTube upload tool</p>
  </header>

  <!-- OVERVIEW -->
  <section>
    <h2>Overview</h2>
    <div class="intro-box">
      Video Farm is an automated pipeline for batch-generating videos and uploading them to YouTube channels.
      It supports multi-account rotation, automatic title generation, and full end-to-end content production workflows —
      with zero manual intervention after setup.<br><br>
      Runs on <strong style="color:var(--text)">Termux</strong> · <strong style="color:var(--text)">Linux</strong> · <strong style="color:var(--text)">macOS</strong>
    </div>
  </section>

  <!-- FEATURES -->
  <section>
    <h2>Features</h2>
    <div class="feature-grid">
      <div class="feature-item">
        <span class="feature-icon">🎬</span>
        <div class="feature-title">Auto Video Generation</div>
        <div class="feature-desc">Batch-produce videos programmatically with pluggable generation backends.</div>
      </div>
      <div class="feature-item">
        <span class="feature-icon">🚀</span>
        <div class="feature-title">Auto YouTube Upload</div>
        <div class="feature-desc">Push videos directly to YouTube via the Data API v3 without manual steps.</div>
      </div>
      <div class="feature-item">
        <span class="feature-icon">🔄</span>
        <div class="feature-title">Account Rotation</div>
        <div class="feature-desc">Distribute uploads evenly across multiple channels automatically.</div>
      </div>
      <div class="feature-item">
        <span class="feature-icon">✏️</span>
        <div class="feature-title">Auto Title Generation</div>
        <div class="feature-desc">Dynamically generate titles for each video at upload time.</div>
      </div>
      <div class="feature-item">
        <span class="feature-icon">📋</span>
        <div class="feature-title">Upload Logging</div>
        <div class="feature-desc">Structured logs track every upload event and account used.</div>
      </div>
      <div class="feature-item">
        <span class="feature-icon">📱</span>
        <div class="feature-title">Termux Compatible</div>
        <div class="feature-desc">Runs fully on Android via Termux — no desktop required.</div>
      </div>
    </div>
  </section>

  <!-- PROJECT STRUCTURE -->
  <section>
    <h2>Project Structure</h2>
    <div class="tree">
<span class="tree-root">video_farm/</span>
<span class="tree-line">│</span>
<span class="tree-line">├── </span><span class="tree-file">farm.py</span><span class="tree-desc">← Main program: generates and uploads videos</span>
<span class="tree-line">├── </span><span class="tree-file">upload.py</span><span class="tree-desc">← YouTube upload module</span>
<span class="tree-line">├── </span><span class="tree-file">client_secret.json</span><span class="tree-desc">← Google OAuth credentials</span>
<span class="tree-line">│</span>
<span class="tree-line">├── </span><span class="tree-dir">generated_videos/</span><span class="tree-desc">← Output directory for generated videos</span>
<span class="tree-line">│</span>
<span class="tree-line">├── </span><span class="tree-file">token_acc1.pickle</span><span class="tree-desc">← OAuth token for channel 1</span>
<span class="tree-line">├── </span><span class="tree-file">token_acc2.pickle</span><span class="tree-desc">← OAuth token for channel 2</span>
<span class="tree-line">│</span>
<span class="tree-line">└── </span><span class="tree-file">README.md</span>
    </div>

    <br>
    <table class="file-table">
      <thead>
        <tr>
          <th>File</th>
          <th>Purpose</th>
        </tr>
      </thead>
      <tbody>
        <tr><td class="file-name">farm.py</td><td>Main program — generates videos and triggers uploads</td></tr>
        <tr><td class="file-name">upload.py</td><td>YouTube Data API v3 upload module</td></tr>
        <tr><td class="file-name">client_secret.json</td><td>Google OAuth 2.0 credentials file</td></tr>
        <tr><td class="file-name">generated_videos/</td><td>Directory where output videos are saved</td></tr>
        <tr><td class="file-name">token_acc1.pickle</td><td>Persisted OAuth token for channel 1</td></tr>
        <tr><td class="file-name">token_acc2.pickle</td><td>Persisted OAuth token for channel 2</td></tr>
      </tbody>
    </table>
  </section>

  <!-- REQUIREMENTS -->
  <section>
    <h2>Requirements</h2>
    <p>Python <strong style="color:var(--text)">3.9+</strong> is required. Install dependencies:</p>

    <pre data-lang="bash"><span class="cm"># Standard (Linux / macOS)</span>
<span class="cmd">pip install</span> google-api-python-client google-auth-oauthlib</pre>

    <pre data-lang="termux"><span class="cm"># Termux (Android)</span>
<span class="cmd">pkg install</span> python
<span class="cmd">pip install</span> google-api-python-client google-auth-oauthlib</pre>
  </section>

  <!-- SETUP -->
  <section>
    <h2>Setup</h2>
    <div class="steps">
      <div class="step">
        <div class="step-num">1</div>
        <div class="step-content">
          <div class="step-title">Obtain YouTube API Credentials</div>
          <p>
            Go to <a href="https://console.cloud.google.com" target="_blank">Google Cloud Console</a> →
            create a project → enable <strong style="color:var(--text)">YouTube Data API v3</strong> →
            create an <strong style="color:var(--text)">OAuth Client ID</strong> →
            download <span class="ic">client_secret.json</span> and place it in the project root.
          </p>
        </div>
      </div>
      <div class="step">
        <div class="step-num">2</div>
        <div class="step-content">
          <div class="step-title">Authorize Accounts</div>
          <p>On first run, a browser window opens for OAuth authorization. Run:</p>
          <pre data-lang="bash"><span class="cmd">python3</span> farm.py</pre>
          <p>After authorization completes, token files are saved automatically:</p>
          <pre data-lang="output"><span class="str">token_acc1.pickle</span>
<span class="str">token_acc2.pickle</span></pre>
          <p style="margin-top:8px;">Subsequent runs will reuse these tokens — no login required.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- RUNNING -->
  <section>
    <h2>Running</h2>
    <pre data-lang="bash"><span class="cmd">python3</span> farm.py</pre>

    <h3>Workflow</h3>
    <div class="flow">
      <div class="flow-step">
        <span class="flow-icon">🎬</span>
        <span class="flow-label">Generate Video</span>
        <span class="flow-sub">generate_video()</span>
      </div>
      <div class="flow-arrow">↓</div>
      <div class="flow-step">
        <span class="flow-icon">💾</span>
        <span class="flow-label">Save to Disk</span>
        <span class="flow-sub">generated_videos/</span>
      </div>
      <div class="flow-arrow">↓</div>
      <div class="flow-step">
        <span class="flow-icon">🔄</span>
        <span class="flow-label">Select Account</span>
        <span class="flow-sub">ACCOUNTS rotation</span>
      </div>
      <div class="flow-arrow">↓</div>
      <div class="flow-step">
        <span class="flow-icon">🚀</span>
        <span class="flow-label">Upload to YouTube</span>
        <span class="flow-sub">upload.py</span>
      </div>
    </div>

    <h3>Example Log Output</h3>
    <div class="log">
      <span class="log-time">[INFO] </span><span class="log-msg">Generated video </span><span class="log-info">video_A1B2C3.mp4</span><br>
      <span class="log-time">[INFO] </span><span class="log-msg">Uploaded </span><span class="log-info">video_A1B2C3.mp4</span><span class="log-msg"> → acc1</span>
    </div>
  </section>

  <!-- MULTI CHANNEL -->
  <section>
    <h2>Multiple Channels</h2>
    <p>Configure your accounts in <span class="ic">farm.py</span>:</p>
    <pre data-lang="python"><span class="kw">ACCOUNTS</span> = [<span class="str">"acc1"</span>, <span class="str">"acc2"</span>]</pre>

    <p>Uploads rotate evenly across all configured accounts:</p>
    <div class="rotation">
      <div class="rot-cell header">Video</div>
      <div class="rot-cell header">Account</div>
      <div class="rot-cell header">Video</div>
      <div class="rot-cell header">Account</div>
      <div class="rot-cell rot-video">Video 1</div>
      <div class="rot-cell rot-acc1">acc1</div>
      <div class="rot-cell rot-video">Video 3</div>
      <div class="rot-cell rot-acc1">acc1</div>
      <div class="rot-cell rot-video">Video 2</div>
      <div class="rot-cell rot-acc2">acc2</div>
      <div class="rot-cell rot-video">Video 4</div>
      <div class="rot-cell rot-acc2">acc2</div>
    </div>
  </section>

  <!-- CUSTOM GENERATION -->
  <section>
    <h2>Custom Video Generation</h2>
    <p>
      A basic <span class="ic">generate_video()</span> example is included by default.
      Replace it with any generation backend to fit your content workflow:
    </p>
    <pre data-lang="python"><span class="cm"># Replace generate_video() with your own backend:</span>
<span class="cm"># ─ AI video generation</span>
<span class="cm"># ─ Image-to-video</span>
<span class="cm"># ─ Text-to-video</span>
<span class="cm"># ─ Auto-editing pipeline</span>
<span class="cm"># ─ Any custom content production workflow</span></pre>
  </section>

  <!-- NOTES -->
  <section>
    <h2>Notes</h2>
    <ul class="note-list">
      <li>Ensure <strong>YouTube Data API v3</strong> is enabled in your Google Cloud project before running.</li>
      <li>Each account must have an active <strong>YouTube channel</strong> associated with it.</li>
      <li>Excessive upload frequency may trigger <strong>YouTube API quota limits</strong> or platform restrictions — upload responsibly.</li>
    </ul>
  </section>

  <!-- LICENSE -->
  <section>
    <h2>License</h2>
    <div class="license-box">
      <div class="license-badge">MIT</div>
      <div class="license-desc">
        This project is open-source under the <strong style="color:var(--text)">MIT License</strong>.<br>
        Free to use, modify, and distribute with attribution.
      </div>
    </div>
  </section>

  <!-- FOOTER -->
  <footer>
    <span><span class="footer-accent">VideoFarm</span> — Automated YouTube Content Pipeline</span>
    <span>MIT License · Python 3.9+</span>
  </footer>

</div>
</body>
</html>
