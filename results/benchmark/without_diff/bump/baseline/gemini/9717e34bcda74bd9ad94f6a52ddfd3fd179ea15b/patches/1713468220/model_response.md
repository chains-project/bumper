```java
import com.jcabi.aspects.Tv;
import org.kohsuke.github.GitHub;

public class MkGithub {
    private final GitHub github;

    public MkGithub(GitHub github) {
        this.github = github;
    }

    public Tv tv() {
        return new Tv(this.github);
    }
}
```