import React, { useState } from 'react';

const Login = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const handleFacebookLogin = async () => {
    // Use the Facebook SDK or a third-party library to handle login
    // Retrieve the access token upon successful login
    const accessToken = 'your_access_token'; // Replace with actual access token

    // Send the token to your backend
    try {
      const response = await fetch('/facebook_login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ accessToken }),
      });

      const data = await response.json();
      if (data.success) {
        setIsLoggedIn(true);
      } else {
        console.error('Login failed:', data.error);
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      {isLoggedIn ? (
        <div>
          <h2>Welcome!</h2>
          {/* Display user information or redirect to a new page */}
        </div>
      ) : (
        <button onClick={handleFacebookLogin}>Login with Facebook</button>
      )}
    </div>
  );
};

export default Login;
