```java
  import com.jcabi.aspects.Tv;
  import java.util.concurrent.Callable;

  public class MkGithub {
    private final Tv tv;

    public MkGithub(Tv tv) {
      this.tv = tv;
    }

    public void add(final String name, final Callable<String> callable) throws Exception {
      this.tv.play(name, callable);
    }
  }
```