```java
  import com.jcabi.aspects.Tv;
  import com.jcabi.github.mock.MkGithub;
  import org.junit.Test;

  public class MkGithubTest {
    @Test
    public void test() {
      Tv tv = new Tv();
      tv.watch(new MkGithub());
    }
  }
```