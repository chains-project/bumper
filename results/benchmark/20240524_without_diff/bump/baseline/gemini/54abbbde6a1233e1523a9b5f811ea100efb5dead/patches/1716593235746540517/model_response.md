```java
import com.jcabi.aspects.Tv;
import com.jcabi.ssh.Ssh;

public class SshTest {

    public static void main(String[] args) throws Exception {
        Ssh ssh = new Ssh("localhost", 22);
        ssh.connect();
        ssh.exec(new Tv());
        ssh.disconnect();
    }
}
```