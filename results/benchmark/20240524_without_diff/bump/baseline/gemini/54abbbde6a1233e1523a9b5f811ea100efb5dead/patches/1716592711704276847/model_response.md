```java
  import com.jcabi.aspects.Tv;
  import com.jcabi.ssh.SshByPassword;

  public class SshByPassword {

      public SshByPassword(String host, int port, String user, String pass) {
          this(host, port, user, pass, null);
      }

      public SshByPassword(String host, int port, String user, String pass, String passphrase) {
          Tv tv = new Tv();
          tv.play("Connecting to " + host + ":" + port + " as " + user + "...");
          try {
              this.ssh = new com.trilead.ssh2.Connection(host, port);
              this.ssh.connect();
              boolean isAuthenticated = this.ssh.authenticateWithPassword(user, pass);
              if (!isAuthenticated) {
                  throw new RuntimeException("Authentication failed.");
              }
          } catch (Exception e) {
              throw new RuntimeException(e);
          }
      }

      public void exec(String command) {
          try {
              this.ssh.exec(command, System.out, System.err);
          } catch (Exception e) {
              throw new RuntimeException(e);
          }
      }

      public void close() {
          try {
              this.ssh.close();
          } catch (Exception e) {
              throw new RuntimeException(e);
          }
      }

      private final com.trilead.ssh2.Connection ssh;
  }
```