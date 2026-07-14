import './Signup.css'

function Signup() {
  //const [count, setCount] = useState(0)

  return (
    <>
      <p>Signup Page</p>
      <form>
        <label>
          Username
          <input type='text' />
        </label>
        <label>
          Emaill Address
          <input type='text' />
        </label>
        <label>
          Password
          <input type='password' />
        </label>
        <label>
          Confirm Password
          <input type='password' />
        </label>
      </form>
    </>
  )
}

export default Signup
