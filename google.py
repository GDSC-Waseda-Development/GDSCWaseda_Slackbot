# google-auth              2.20.0
# google-auth-oauthlib     1.0.0

# GOOGLE_API_KEY

import google.auth

credentials, project = google.auth.default(
    scopes=['https://www.googleapis.com/auth/cloud-platform'])
