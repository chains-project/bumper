```java
  import com.jcabi.aspects.Tv;
  import com.jcabi.ssh.Ssh;
  import com.jcabi.ssh.SshByPassword;

  public class SshByPassword {

    private final Ssh ssh;

    public SshByPassword(String host, String user, String pass) {
      this.ssh = new SshByPassword(host, user, pass);
    }

    public Tv tv() {
      return new Tv(this.ssh);
    }
  }
```