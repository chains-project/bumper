```java
public com.jcabi.github.Repo randomRepo() throws java.io.IOException {
    int tv = 20;
    return this.repos().create(new com.jcabi.github.Repos.RepoCreate(org.apache.commons.lang3.RandomStringUtils.randomAlphanumeric(tv), true));
}
```