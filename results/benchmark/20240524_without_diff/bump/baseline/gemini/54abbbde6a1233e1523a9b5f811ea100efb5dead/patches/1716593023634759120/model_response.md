```java
  import com.jcabi.aspects.Tv;

  import java.io.IOException;

  public class SshByPassword extends AbstractSsh {
      private final String username;
      private final String password;

      public SshByPassword(final String host, final int port, final String username, final String password) {
          super(host, port);
          this.username = username;
          this.password = password;
      }

      @Override
      protected void setup() throws IOException {
          final Tv tv = new Tv();
          tv.play("Connecting to " + this.host + ":" + this.port + " as " + this.username);
          super.setup();
          tv.play("Connected");
          this.auth.publickey(this.username, new String[]{this.password});
          tv.play("Authenticated");
      }
  }
```