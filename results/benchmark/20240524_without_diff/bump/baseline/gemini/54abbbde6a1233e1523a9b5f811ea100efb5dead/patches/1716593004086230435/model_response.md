```java
import com.jcabi.aspects.Tv;
import com.jcabi.ssh.SshByPassword;

public class SshByPasswordTest {

    public static void main(String[] args) throws Exception {
        Tv tv = new Tv();
        SshByPassword ssh = new SshByPassword("localhost", 22, "user", "password");
        ssh.exec(tv);
    }
}
```