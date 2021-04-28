import github from './github.svg';

function Title() {
    return (
        <div>
            <h1>
                词语接龙
            </h1>
            <div>
                [explore hsk]
            </div>
            <div>
                Browse Chinese vocabulary by etymology
            </div>
        </div>
    )
}


function Nav() {
    return (
        <div>
            {/* think about settings those to <button></button> tags */}
            <div>random</div> 
            <div>search</div>
            <div>about</div>
            <div>settings</div>
            <div>
                <a href="https://github.com/syltruong/explorehsk" target="_blank">
                    <img src={github} alt="github octocat" />
                </a>
            </div>
        </div>
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