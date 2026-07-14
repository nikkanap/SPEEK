import Header from '../../components/Header'
import './Signup.css'

function Signup() {
  //const [count, setCount] = useState(0)

  const handleSignup = () => {
    alert("Pressed signup button")
  }

  return (
    <>
      <Header />
      <p>Signup Page</p>
      <form action={handleSignup} className='form-container'>
        <label>
          Username
          <input 
            type='text' 
            placeholder='Create a username'
          />
        </label>
        <label>
          Email Address
          <input 
            type='text' 
            placeholder='Add email address'
          />
        </label>
        <label>
          Password
          <input 
            type='password' 
            placeholder='Create password'
          />
        </label>
        <label>
          Confirm Password
          <input 
            type='password' 
            placeholder='Confirm password'
          />
        </label>
        <div className='form-buttons'>
          <button type='submit'>Signup</button>
          <button type='reset'>Clear Form</button>
        </div>
      </form>
    </>
  )
}

export default Signup
