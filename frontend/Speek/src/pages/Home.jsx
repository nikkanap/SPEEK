//import { useState } from 'react'
import { Link } from 'react-router-dom'
import Header from '../components/Header'
import './Home.css'

function Home() {
  //const [count, setCount] = useState(0)

  return (
    <>
      <Header />
      <h1>SPEEK - Chat Messaging Application</h1>
      <Link to='login/'>Login</Link>
      <Link to='signup/'>Signup</Link>
    </>
  )
}

export default Home
