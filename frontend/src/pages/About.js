import './About.css'

function About() {
    return (
        <section className={"en"}>
            <h2>About</h2>
            <p>
                This webapp is meant to help you review your Chinese words.
            </p>
            <p>
                It is based on the vocabulary list of the <a href="https://en.wikipedia.org/wiki/Hanyu_Shuiping_Kaoshi" target="_blank" rel="noreferrer">HSK (汉语水平考试)</a>, 
                the standard Chinese language test for foreigners, thus making sure that the vocabulary list is relevant.
            </p>
            <p>
                It is up-to-date with the latest 2021 HSK reform as well as with the introduction of levels 7-9.
            </p>
            <p>
                The idea is to let you browse words according to usage of characters and meaning,
                thus helping you to create a context around each word of your vocabulary,
                and develop your word formation skills (造词).
            </p>
            <h2>
                Questions? Issues? Suggestions?
            </h2>
            <p>
                Please visit the <a href="https://github.com/syltruong/explorehsk" target="_blank" rel="noreferrer">github project</a>, 
                and open an issue, or even a pull request!
            </p>
        </section>
    )
}

export default About