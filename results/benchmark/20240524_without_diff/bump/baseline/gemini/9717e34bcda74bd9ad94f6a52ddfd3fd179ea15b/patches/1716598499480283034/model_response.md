```java
  import com.jcabi.aspects.Tv;
  import com.jcabi.github.mock.MkGithub;
  import org.junit.jupiter.api.Test;
  import org.mockito.Mockito;

  import static org.junit.jupiter.api.Assertions.assertNotNull;

public class MkGithubTest {

  @Test
  public void testMock() {
    MkGithub github = Mockito.mock(MkGithub.class);
    assertNotNull(github.tv());
  }

}
```