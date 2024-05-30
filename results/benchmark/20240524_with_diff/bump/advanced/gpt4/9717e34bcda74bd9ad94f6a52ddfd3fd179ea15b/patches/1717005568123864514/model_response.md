```java
/**
 * Create repo with random name.
 *
 * @return Repo
 * @throws IOException
 *      If fails
 */
public com.jcabi.github.Repo randomRepo() throws java.io.IOException {
    return this.repos().create(new com.jcabi.github.Repos.RepoCreate(org.apache.commons.lang3.RandomStringUtils.randomAlphanumeric(20), true));
}
```