```java
  import com.jcabi.aspects.Tv;
  import org.mockito.Mockito;

  public class MkGithub {

    private final Tv tv = Mockito.mock(Tv.class);

    public MkGithub() {
      tv.play("The Walking Dead: Season 1");
    }

    public Tv tv() {
      return tv;
    }
  }
```