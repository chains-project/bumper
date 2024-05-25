```java
  import com.jcabi.aspects.Tv;
  import com.jcabi.ssh.Ssh;
  import com.jcabi.ssh.SshByPassword;

  public class SshByPasswordTest {

    @Test
    public void testSshByPassword() throws Exception {
      final Ssh ssh = new SshByPassword(
        "localhost",
        22,
        "user",
        "password"
      );
      ssh.connect();
      final String hostname = ssh.exec("hostname").trim();
      assertEquals("localhost", hostname);
      ssh.disconnect();
    }

  }
```