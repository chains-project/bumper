```java
  import com.jcabi.aspects.Tv;
  import com.jcabi.github.mock.MkGithub;
  import org.junit.jupiter.api.Test;

  import static org.mockito.Mockito.mock;
  import static org.mockito.Mockito.when;

  @Test
  public void testMock() {
    MkGithub github = mock(MkGithub.class);
    when(github.tv()).thenReturn(new Tv(1, "title"));
    github.tv();
  }
```