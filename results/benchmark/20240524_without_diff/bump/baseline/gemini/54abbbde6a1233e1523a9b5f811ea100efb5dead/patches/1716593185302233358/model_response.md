```java
  import com.jcabi.aspects.Tv;
import com.jcabi.ssh.SshByPassword;

  public class MySshByPassword extends SshByPassword {

    public MySshByPassword(String host, String user, String pass) {
      super(host, user, pass);
    }

    @Override
    public Tv tv() {
      return new Tv();
    }
  }
```