import {Link} from 'react-router-dom'

import github from './github.svg';
import './Header.css';

function Title() {
    return (
        <div className={'title'}>
            <h1 className={'zh'}>
                词语接龙
            </h1>
            <h2 className={'en'}>
                [explore hsk]
            </h2>
            <h3 className={'en'}>
                Browse Chinese vocabulary by etymology
            </h3>
        </div>
    )
}


function Nav(props) {
    const {onRandom} = props
    return (
        <nav>
            <Link to="/">
                <button className={'en'} onClick={onRandom}>random</button> 
            </Link>
            
            <button className={'en'}>search</button>
            
            <Link to="/about">
                <button className={'en'}>about</button>
            </Link>
            
            <button className={'en'}>settings</button>
            
            <button>
                <a href="https://github.com/syltruong/explorehsk" target="_blank">
                    <img src={github} alt="github octocat" />
                </a>
            </button>
        </nav>
    )
}

function Header(props) {
    const {onRandom} = props
    return (
        <header>
            <Title />
            <Nav onRandom={onRandom}/>
        </header>
    )
}

export default Header