### Different types of auth token and how they works

- Auth token
- Session token
- JSON Web Token (JWT)
- Refresh token

Also, know about

- Basic
- Bearer

#### Putting them in right category

- **Auth Token**: It's an `umbrella` term, any piece of data that proves a user is authenticated is called auth token
- **Basic**: It's a `transport` mechanism. It sends raw `username:password` encoded in base64 with every single request.
  - So it's should never be used for front-end app. It's mostly used for internal `machine-to-machine` communication. Or we we login.
- **Bearer Token**: bearer means 'give access to whoever carries this'. This is the envelop for JWT
  - Generally formatted in Header as `Authorization: Bearer <the_jwt_token>`

#### Let's talk about the real tokens now

- **Session Token**

  Also known as a Session ID, this is the Stateful approach to security.
  - How it works: When you log in, the server creates a file (a "session") in its database or memory. It then sends you a random string of characters (the Session Token).
  - The Verification: Every time you make a request, you send that string back. The server looks it up in its "filing cabinet" to see who you are.
  - The Analogy: `Like a coat check`. You give the attendant your coat, they give you a numbered ticket. The ticket has no value on its own, but the attendant uses it to find your specific coat in their closet.

- **JWT**

  JSON Web Token is a Stateless approach. Unlike a session token, the server doesn't need to look anything up in a database.
  - How it works: All your user info (User ID, roles, expiration date) is encoded directly into the token itself and signed by the server so it can't be tampered with.
  - The Verification: The server just checks the digital signature. If the signature is valid, the server trusts the information inside.
  - The Analogy: `Smart card` Like a high-tech Driver's License. It has your name, birthdate, and photo on it. A bouncer doesn't need to call the DMV to know who you are; they just look at the license and check the holographic seal for authenticity.

- **Refresh Token**

  To keep things secure, Access Tokens (which are usually JWTs) are designed to expire very quickly—sometimes in just 15 minutes. This is where the Refresh Token comes in.
  - The Problem: If your access token expires every 15 minutes, you'd have to log in with your password constantly. That’s a terrible user experience.
  - The Solution: When you log in, you get two tokens:
    - Access Token: Short-lived (15 mins). Used for every request.
    - Refresh Token: Long-lived (days or weeks). Used only to get a new access token.
  - The Analogy: You're at a hotel. Your Access Token is your key card—it lets you into your room, but it expires every 24 hours. Your Refresh Token is the voucher you take to the front desk to get your key card reactivated without having to show your passport and credit card all over again.
