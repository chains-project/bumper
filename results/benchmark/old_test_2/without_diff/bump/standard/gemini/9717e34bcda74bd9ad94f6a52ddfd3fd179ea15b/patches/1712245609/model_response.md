```java
import static com.jcabi.github.mock.Tv.TWENTY;
...
return this.repos().create(new com.jcabi.github.Repos.RepoCreate(org.apache.commons.lang3.RandomStringUtils.randomAlphanumeric(TWENTY), true));
```