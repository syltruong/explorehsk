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


function Nav() {
    return (
        <nav>
            {/* think about settings those to <button></button> tags */}
            <button className={'en'}>random</button> 
            <button className={'en'}>search</button>
            <button className={'en'}>about</button>
            <button className={'en'}>settings</button>
            <button>
                <a href="https://github.com/syltruong/explorehsk" target="_blank">
                    <img src={github} alt="github octocat" />
                </a>
            </button>
        </nav>
    )
}

function Header() {
    return (
        <header>
            <Title />
            <Nav />
        </header>
    )
}

export default Header