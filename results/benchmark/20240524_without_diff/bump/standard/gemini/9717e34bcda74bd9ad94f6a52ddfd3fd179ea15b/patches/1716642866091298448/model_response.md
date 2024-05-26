```java
public com.jcabi.github.Repo randomRepo() throws java.io.IOException {
    int length = 20;
    boolean letters = true;
    boolean numbers = true;
    String generatedString = org.apache.commons.lang3.RandomStringUtils.random(length, letters, numbers);
    return this.repos().create(new com.jcabi.github.Repos.RepoCreate(generatedString, true));
}
```