```java
import com.jcabi.aspects.Tv;
import com.jcabi.ssh.Shell;
import com.jcabi.ssh.Ssh;
import com.jcabi.ssh.SshByPassword;

import java.io.IOException;

public class Ssh {

    private final Shell shell;

    /**
     * Construct SSH client.
     * @param host Hostname
     * @param port Port
     * @param user Username
     * @param pass Password
     * @throws IOException If there is an I/O problem
     */
    public Ssh(String host, int port, String user, String pass) throws IOException {
        this.shell = new SshByPassword(host, port, user, pass).shell();
    }

    /**
     * Execute command.
     * @param cmd Command to execute
     * @return Output of the command
     * @throws IOException If there is an I/O problem
     */
    public String exec(String cmd) throws IOException {
        return this.shell.exec(cmd);
    }

    /**
     * Execute command.
     * @param cmd Command to execute
     * @param args Arguments to the command
     * @return Output of the command
     * @throws IOException If there is an I/O problem
     */
    public String exec(String cmd, String... args) throws IOException {
        return this.shell.exec(cmd, args);
    }

    /**
     * Close the connection.
     * @throws IOException If there is an I/O problem
     */
    public void close() throws IOException {
        this.shell.close();
    }

    /**
     * Main.
     * @param args Command line arguments
     * @throws IOException If there is an I/O problem
     */
    public static void main(String[] args) throws IOException {
        Tv.INSTANCE.on();
        try (Ssh ssh = new Ssh("localhost", 2222, "user", "pass")) {
            System.out.println(ssh.exec("ls -l"));
        }
    }
}
```