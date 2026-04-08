import sys
import codecs

try:
    with codecs.open("d:\\Terraform IaC\\iac-generator\\backend\\app.py", "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Add mock users store & routes
    backend_code = """
# ---------------------------------------------------------------------------
# Auth Flow (Mock setup)
# ---------------------------------------------------------------------------
mock_users = {}  # In-memory store: {username: password}

@app.route("/api/signup", methods=["POST"])
def api_signup():
    data = request.get_json()
    username = data.get("username", "").strip()
    password = data.get("password", "").strip()
    if not username or not password:
        return jsonify({"success": False, "error": "Invalid input"})
    if username in mock_users:
        return jsonify({"success": False, "error": "User already exists"})
    mock_users[username] = password
    return jsonify({"success": True})

@app.route("/api/login", methods=["POST"])
def api_login():
    data = request.get_json()
    username = data.get("username", "").strip()
    password = data.get("password", "").strip()
    if mock_users.get(username) == password:
        return jsonify({"success": True})
    return jsonify({"success": False, "error": "Invalid credentials"})

"""
    content = content.replace('if __name__ == "__main__":', backend_code + 'if __name__ == "__main__":')

    # 2. Add CSS
    css_code = """
        /* New Landing Page Styles */
        .landing-header { display: flex; justify-content: space-between; align-items: center; padding: 10px 40px; border-bottom: 1px solid #222; margin-bottom: 70px; width: 100%; max-width: 1200px; }
        .landing-header .logo { font-size: 24px; font-weight: bold; display: flex; align-items: center; gap: 10px; }
        .landing-header .nav-links { display: flex; gap: 30px; align-items: center; font-size: 14px; color: #aaa; font-weight: 500;}
        .landing-header .nav-links a { color: #ccc; text-decoration: none; cursor: pointer; transition: color 0.2s; }
        .landing-header .nav-links a:hover { color: #fff; }
        .landing-hero { text-align: center; max-width: 800px; margin: 0 auto; display: flex; flex-direction: column; align-items: center; }
        .hero-title { font-size: 56px; font-weight: 800; line-height: 1.1; margin-bottom: 24px; letter-spacing: -1px; }
        .hero-title .gradient-text { background: linear-gradient(90deg, #f59e0b, #ec4899, #8b5cf6); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .hero-subtitle { font-size: 18px; color: #999; line-height: 1.6; margin-bottom: 40px; max-width: 600px; }
        .hero-buttons { display: flex; gap: 16px; justify-content: center; }
        .btn-primary { background: #8b5cf6; padding: 14px 28px; font-size: 16px; border-radius: 8px; color: #fff; font-weight: 600; border: none; cursor: pointer; transition: background 0.2s, transform 0.1s; box-shadow: 0 4px 14px 0 rgba(139, 92, 246, 0.39); }
        .btn-primary:hover { background: #7c3aed; transform: translateY(-1px); }
        .btn-secondary { background: transparent; padding: 14px 28px; font-size: 16px; border-radius: 8px; color: #a78bfa; font-weight: 600; border: 1px solid rgba(139, 92, 246, 0.5); cursor: pointer; transition: background 0.2s; }
        .btn-secondary:hover { background: rgba(139, 92, 246, 0.1); }
        .auth-modal { background: #111; border: 1px solid #222; border-radius: 12px; width: 90%; max-width: 400px; padding: 30px; display: none; }
        .auth-modal h2 { margin-bottom: 20px; font-size: 24px; text-align: center; }
        .auth-modal input { margin-bottom: 15px; }
        .auth-modal button { width: 100%; margin-bottom: 10px; }
        .auth-switch { color: #8b5cf6; font-size: 14px; cursor: pointer; text-align: center; display: block; margin-top: 10px; }
        #auth-overlay { pointer-events: none; opacity: 0; transition: opacity 0.2s; display: flex; }
        #auth-overlay.open { pointer-events: auto; opacity: 1; }
    </style>
"""
    content = content.replace("    </style>", css_code)

    # 3. Add HTML Body
    html_body_replacement = """
<body>
    <!-- Landing Page -->
    <div id="landing-page" style="width: 100%; display: flex; flex-direction: column; align-items: center; position: absolute; inset: 0; background: #0a0a0a; z-index: 10;">
        <div class="landing-header">
            <div class="logo">
                <!-- Logo will be finalized and uploaded later -->
                <img src="#" alt="" style="display:none;" id="logo-img">
            </div>
            <div class="nav-links">
                <a>Slack</a>
                <a>Registry</a>
                <a>Contact Us</a>
                <button class="btn-primary" onclick="openAuthModal('login')" style="padding: 8px 16px; font-size: 14px; box-shadow: none;">Sign In</button>
            </div>
        </div>
        <div class="landing-hero">
            <h1 class="hero-title"><span class="gradient-text">Modern Infrastructure as Code,</span><br>Now with Agentic AI.</h1>
            <p class="hero-subtitle">The AI infrastructure platform developers trust and teams deploy with. Any cloud, one prompt. Automated, integrated and notified by default.</p>
            <div class="hero-buttons">
                <button class="btn-primary" onclick="openAuthModal('signup')">Get Started</button>
                <button class="btn-secondary">Contact Us</button>
            </div>
        </div>
        
        <!-- Auth Modals -->
        <div id="auth-overlay" class="modal-overlay" onclick="closeAuthModal(event)">
            <div class="auth-modal" id="login-modal" onclick="event.stopPropagation()">
                <h2>Sign In</h2>
                <label>Username</label>
                <input type="text" id="login-user">
                <label>Password</label>
                <input type="password" id="login-pass">
                <button class="btn-primary" onclick="doAuth('login')">Login</button>
                <span class="auth-switch" onclick="openAuthModal('signup')">Don't have an account? Sign Up</span>
                <div id="login-error" style="color: #ef4444; font-size: 14px; margin-top: 10px; display: none; text-align: center;"></div>
            </div>
            <div class="auth-modal" id="signup-modal" onclick="event.stopPropagation()">
                <h2>Sign Up</h2>
                <label>Username</label>
                <input type="text" id="signup-user">
                <label>Password</label>
                <input type="password" id="signup-pass">
                <button class="btn-primary" onclick="doAuth('signup')">Create Account</button>
                <span class="auth-switch" onclick="openAuthModal('login')">Already have an account? Sign In</span>
                <div id="signup-error" style="color: #ef4444; font-size: 14px; margin-top: 10px; display: none; text-align: center;"></div>
            </div>
        </div>
    </div>

    <!-- Main Content App Container -->
    <div id="app-container" style="display: none; width: 100%; max-width: 900px; flex-direction: column; align-items: center;">
        <div style="width: 100%; display: flex; justify-content: flex-end; margin-bottom: 20px;">
            <button onclick="logout()" style="background: transparent; border: 1px solid #333; color: #888; padding: 6px 12px; font-size: 13px; cursor: pointer; border-radius: 6px;">Logout</button>
        </div>
"""

    original_body_start = '<body>\\n    <a href="https://app.slack.com/client/T0AM7JC0WBW/C0AMAS20ZM2" target="_blank" class="slack-btn" title="Open Slack Logs">'
    content = content.replace(original_body_start, html_body_replacement + '\\n    <a href="https://app.slack.com/client/T0AM7JC0WBW/C0AMAS20ZM2" target="_blank" class="slack-btn" title="Open Slack Logs">')

    # Close app container before github modals
    app_container_close = """
    </div> <!-- End app-container -->

    <!-- Azure Modals -->
"""
    content = content.replace("    <!-- Azure Modals -->", app_container_close)

    # 4. JS logic
    js_code = """
    <script>
        // Auth Logic
        let currentUser = localStorage.getItem("iac_user");
        if (currentUser) {
            document.getElementById("landing-page").style.display = "none";
            document.getElementById("app-container").style.display = "flex";
        }

        function openAuthModal(type) {
            document.getElementById("auth-overlay").classList.add("open");
            document.getElementById("login-modal").style.display = type === 'login' ? 'block' : 'none';
            document.getElementById("signup-modal").style.display = type === 'signup' ? 'block' : 'none';
            document.getElementById("login-error").style.display = "none";
            document.getElementById("signup-error").style.display = "none";
        }

        function closeAuthModal(e) {
            if (e && e.target !== document.getElementById('auth-overlay')) return;
            document.getElementById("auth-overlay").classList.remove("open");
            document.getElementById("login-modal").style.display = 'none';
            document.getElementById("signup-modal").style.display = 'none';
        }

        async function doAuth(action) {
            const userStr = document.getElementById(action + "-user").value.trim();
            const passStr = document.getElementById(action + "-pass").value.trim();
            const errDiv = document.getElementById(action + "-error");
            
            if(!userStr || !passStr) {
                errDiv.textContent = "Please fill all fields.";
                errDiv.style.display = "block";
                return;
            }
            
            const btn = document.querySelector("#" + action + "-modal .btn-primary");
            const btnOrigText = btn.textContent;
            btn.innerHTML = '<span class="spinner"></span>Processing...';
            btn.disabled = true;

            try {
                const res = await fetch('/api/' + action, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ username: userStr, password: passStr })
                });
                const data = await res.json();
                if(data.success) {
                    localStorage.setItem("iac_user", userStr);
                    closeAuthModal();
                    document.getElementById("landing-page").style.display = "none";
                    document.getElementById("app-container").style.display = "flex";
                } else {
                    errDiv.textContent = data.error || "Authentication failed.";
                    errDiv.style.display = "block";
                }
            } catch(e) {
                errDiv.textContent = "Network error. Make sure the backend is running.";
                errDiv.style.display = "block";
            } finally {
                btn.textContent = btnOrigText;
                btn.disabled = false;
            }
        }

        function logout() {
            localStorage.removeItem("iac_user");
            document.getElementById("app-container").style.display = "none";
            document.getElementById("landing-page").style.display = "flex";
            if (typeof switchFlow === "function") switchFlow('main'); 
            document.getElementById("login-user").value = "";
            document.getElementById("login-pass").value = "";
            document.getElementById("signup-user").value = "";
            document.getElementById("signup-pass").value = "";
        }
"""
    content = content.replace("    <script>", js_code)

    with codecs.open("d:\\Terraform IaC\\iac-generator\\backend\\app.py", "w", encoding="utf-8") as f:
        f.write(content)

    print("Patched app.py successfully!")
except Exception as e:
    print(f"Error: {e}")
