/* This is where we store the payloads for POST apis*/

// login payload for API
export const loginPayload = (
  username,
  password
) => {
  const payload = {
    username,
    password
  }

  return payload
}

// signup payload for API
export const signupPayload = (
  username,
  email,
  password
) => {
  const payload = {
    username,
    email,
    password,
  }

  return payload
}
