```java
/**
 * Create repo with random name.
 *
 * @return Repo
 * @throws IOException
 * 		If fails
 */
public com.jcabi.github.Repo randomRepo() throws java.io.IOException {
    int length = 20; // Tv.TWENTY is not found, so we replace it with a local variable with the same value.
    return this.repos().create(new com.jcabi.github.Repos.RepoCreate(org.apache.commons.lang3.RandomStringUtils.randomAlphanumeric(length), true));
}
```