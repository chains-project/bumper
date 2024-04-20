Here's the patched `randomRepo()` method that fixes the error:

```java
import com.jcabi.github.Repos;
import com.jcabi.github.RepoCreate;
import java.io.IOException;
import java.util.Random;
import static java.util.concurrent.TimeUnit.SECONDS;
import static java.lang.String.format;

public com.jcabi.github.Repo randomRepo() throws java.io.IOException {
    Random random = new Random();
    return this.repos().create(new com.jcabi.github.Repos.RepoCreate(
        format("random-%d", random.nextInt(100_000)), true));
}
```

The `Tv` class is removed in the new library version. I replaced it with a `Random` class to generate a random number for the repository name. The `RandomStringUtils` class is also removed, so I used `String.format()` to create the repository name.