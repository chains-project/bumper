```java
  import com.jcabi.aspects.Tv;
  import com.jcabi.log.Logger;
  import java.io.IOException;
  import java.nio.file.Path;
  import java.nio.file.Paths;
  import java.util.concurrent.TimeUnit;

  public class MkGithub extends Github {
    private static final Path TV = Paths.get(System.getProperty(
        "user.home"), ".jcabi", "tv");
    private transient final Tv tv;

    public MkGithub(String user, String password) {
      super(user, password);
      this.tv = new Tv(TV);
    }

    @Override
    public void close() throws IOException {
      super.close();
      try {
        this.tv.close();
      } catch (InterruptedException ex) {
        Logger.warn(this, ex, "Failed to close TV");
      }
    }

    public void start() {
      this.tv.start();
    }

    public void stop() {
      try {
        this.tv.stop(10, TimeUnit.SECONDS);
      } catch (InterruptedException ex) {
        Logger.warn(this, ex, "Failed to stop TV");
      }
    }
  }
```