```java
import com.jcabi.aspects.Tv;
import com.jcabi.ssh.SshByPassword;

public class SshByPasswordTest {

    public void testSshByPassword() throws Exception {
        // Create a new SshByPassword object
        SshByPassword ssh = new SshByPassword("localhost", 22, "user", "password");

        // Create a new Tv object
        Tv tv = new Tv();

        // Set the TV's channel to 1
        tv.setChannel(1);

        // Assert that the TV's channel is 1
        assertEquals(1, tv.getChannel());

        // Close the SSH connection
        ssh.close();
    }
}
```