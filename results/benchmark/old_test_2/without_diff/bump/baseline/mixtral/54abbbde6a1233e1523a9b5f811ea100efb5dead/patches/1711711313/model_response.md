Here is a fixed version of the `session()` method:
```java
import org.apache.commons.io.output.Tee;
import org.apache.commons.lang3.time.Duration;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import com.google.common.base.CharMatcher;
import com.google.common.base.Function;
import com.google.common.base.Joiner;
import com.google.common.base.Throwables;
import com.google.common.io.Files;
import com.jcabi.ssh.JschLogger;
import com.jcabi.ssh.JschSession;
import com.jcabi.ssh.Key;
import com.jcabi.ssh.Key.Rsa;
import com.jcabi.ssh.Session;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.UncheckedIOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;
import java.security.GeneralSecurityException;
import java.util.concurrent.TimeUnit;
import javax.annotation.CheckForNull;
import javax.annotation.Nonnull;
import javax.annotation.ParametersAreNonnullByDefault;
import ma.jcabi.log.Der;
import net.schmizz.sshj.sftp.KeyExchange;
import net.schmizz.sshj.sftp.KeyExchange.Algorithm;
import net.schmizz.sshj.sftp.KeyExchange.Factory;
import net.schmizz.sshj.sshj.SSHClient;
import net.schmizz.sshj.sshj.transport.KeyPairProvider;
import net.schmizz.sshj.transport.TransportException;
import net.schmizz.sshj.transport.keyfile.KeyFiles;
import net.schmizz.sshj.userauth.UserAuth;
import net.schmizz.sshj.userauth.method.AuthPassword;
import net.schmizz.sshj.userauth.method.AuthPublickey;
import net.schmizz.sshj.userauth.method.UserAuthPublicKey;
import net.schmizz.sshj.xfer.FileSystemFile;
import static com.google.common.base.Preconditions.checkNotNull;
import static java.util.concurrent.TimeUnit.SECONDS;
import static net.schmizz.sshj.transport.Transport.DisconnectReason.HOST_KEY_NOT_VERIFIABLE;
import static net.schmizz.sshj.transport.Transport.DisconnectReason.PROTOCOL_ERROR;

@ParametersAreNonnullByDefault
public class Ssh {

    ...

    @RetryOnFailure(
        attempts = Tv.SEVEN,
        delay = 1,
        unit = TimeUnit.MINUTES,
        verbose = false,
        types = IOException.class
    )
    protected Session session() throws IOException {
        final File file = File.createTempFile("jcabi-ssh", ".key");
        try {
            JschLogger jschLogger = new JschLogger();
            JSch jsch = new JSch();
            jsch.setLogger(jschLogger);
            Rsa rsa = Rsa.generate(2048);
            final String publicKey = rsa.publicKey();
            final String privateKey = rsa.privateKey();
            Files.write(file.toPath(), privateKey.getBytes(StandardCharsets.UTF_8));
            jsch.addIdentity(file.getAbsolutePath());
            jsch.setHostKeyRepository(new EasyRepo());
            Session session = jsch.getSession(this.getLogin(), this.getAddr(), this.getPort());
            session.setConfig("StrictHostKeyChecking", "no");
            session.connect();
            UserAuth auth = session.getUserInfo().getAuthenticator();
            if (auth instanceof UserAuthPublicKey) {
                UserAuthPublicKey authPublicKey = (UserAuthPublicKey) auth;
                authPublicKey.addIdentity(publicKey, privateKey);
            } else if (auth instanceof AuthPublickey) {
                AuthPublickey authPublickey = (AuthPublickey) auth;
                authPublickey.addIdentity(publicKey, privateKey);
            } else if (auth instanceof AuthPassword) {
                AuthPassword authPassword = (AuthPassword) auth;
                authPassword.authenticate(this.getLogin(), this.getPassword());
            }
            return new JschSession(session);
        } catch (GeneralSecurityException | TransportException ex) {
            throw new IOException(ex);
        } finally {
            Files.deleteIfExists(file.toPath());
        }
    }

    ...

}
```
The main changes are:

* Use the `Jsch` library directly, instead of the deprecated `JschSession` class.
* Generate a new RSA key pair using the `Rsa` class.
* Write the private key to a temporary file.
* Use the `addIdentity` method of `Jsch` to add the RSA key pair.
* Connect to the server using the `getSession` method of `Jsch`.
* Set the `StrictHostKeyChecking` configuration option to `"no"`.
* Authenticate using the appropriate `UserAuth` method based on the type of authentication used by the server.
* Return a new `JschSession` instance using the connected `Session` instance.

Note that this is just one way to fix the issue. There may be other ways to modify the client code to avoid the error.