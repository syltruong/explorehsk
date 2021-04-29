import './About.css'

function About() {
    return (
        <div>
            <h2>About</h2>
            <p>
                This webapp is meant to help you review your HSK vocabulary.
                The idea is to recommend, for every flashcard, related flashcards.
            </p>
            <p>
                Closeness of vocabulary is determined by usage of characters and meaning.
            </p>
            <h2>
                Questions? Issues? Suggestions?
            </h2>
            <p>
                Please visit the
                <a href="https://github.com/syltruong/explorehsk" target="_blank"> github project</a>, 
                and open an issue, or even a pull request!
            </p>
        </div>
    )
}

export default About