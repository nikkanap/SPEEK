import Header from '../../components/Header'
import './Login.css'
import './Forms.css'

function Login() {
  //const [count, setCount] = useState(0)
  const handleLogin = () => {
    alert('Pressed login button')
  }

  return (
    <>
    <Header />
      <h1>Login Page</h1>
      <form action={handleLogin} className='form-container'>
        <label>
          Username
          <input 
            type='text'
            placeholder='Enter username'
          />
        </label>
        <label>
          Password
          <input 
            type='password' 
            placeholder='Enter password'
          />
        </label>
        <div className='form-buttons'>
          <button type='submit'>Login</button>
          <button type='reset'>Clear Form</button>
        </div>
      </form>
    </>
  )
}

export default Login
