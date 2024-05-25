```java
  import com.jcabi.aspects.Tv;
  import org.mockito.Mockito;

  public class MkGithub {

    @Tv
    public void testCreateRepo() {
      final MkGithub github = Mockito.mock(MkGithub.class);
      github.createRepo(Mockito.anyString());
      Mockito.verify(github).createRepo(Mockito.anyString());
    }

  }
```