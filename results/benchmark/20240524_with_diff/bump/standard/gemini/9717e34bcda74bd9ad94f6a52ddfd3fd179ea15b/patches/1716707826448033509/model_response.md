```java
/**
 * Create repo with random name.
 *
 * @return Repo
 * @throws IOException
 * 		If fails
 */
public com.jcabi.github.Repo randomRepo() throws java.io.IOException {
    final int length = 20;
    final String name = org.apache.commons.lang3.RandomStringUtils.randomAlphanumeric(length);
    return this.repos().create(new com.jcabi.github.Repos.RepoCreate(name, true));
}
```