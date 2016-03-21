# Run a test server.
from app import app
app.run(host='staging.darwin-prod.com', port=8080, debug=True)
