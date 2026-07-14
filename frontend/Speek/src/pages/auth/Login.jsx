import './Login.css'

function Login() {
  //const [count, setCount] = useState(0)

  return (
    <>
      <p>Login Page</p>
      <form>
        <label>
          Username
          <input type='text' />
        </label>
        <label>
          Password
          <input type='password' />
        </label>
      </form>
    </>
  )
}

export default Login
