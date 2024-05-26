Here is a possible patch for the failing client code:

```
import static com.jcabi.github.Tv.*;

public com.jcabi.github.Repo randomRepo() throws java.io.IOException {
    int twenty = TWENTY;
    return this.repos().create(new com.jcabi.github.Repos.RepoCreate(org.apache.commons.lang3.RandomStringUtils.randomAlphanumeric(twenty), true));
}
``
```