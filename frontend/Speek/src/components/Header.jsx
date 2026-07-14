import './Header.css'
import { Link } from 'react-router-dom'

function Header() {
  return (
    <>
      {/*Pages adjusted if required*/}
      <div className='header-container'>
        <h1>SPEEK</h1> 
        <div className='header-links'>
          <Link to='/'>Home</Link>
          <Link to='../login/'>Login</Link> 
        </div>
      </div>
    </>
  )
}

export default Header
