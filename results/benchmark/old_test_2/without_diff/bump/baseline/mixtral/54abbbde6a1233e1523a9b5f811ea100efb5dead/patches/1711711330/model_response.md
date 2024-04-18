Here is a fixed version of the `session()` method:
```java
import com.google.common.base.Charsets;
import com.google.common.io.Files;
import com.jcabi.github.ErrorResponse;
import com.jcabi.github.Github;
import com.jcabi.github.GithubException;
import com.jcabi.github.ImmutableHttp;
import com.jcabi.github.Repo;
import com.jcabi.github.RepoCollaborator;
import com.jcabi.github.ServerUrl;
import com.jcabi.github.auth.GithubTokenAuthenticator;
import com.jcabi.ssh.JSch;
import com.jcabi.ssh.JschLogger;
import com.jcabi.ssh.Key;
import com.jcabi.ssh.Key.Private;
import com.jcabi.ssh.KeyGen;
import com.jcabi.ssh.Session;
import java.io.ByteArrayInputStream;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.NoSuchAlgorithmException;
import java.security.interfaces.RSAPrivateKey;
import java.security.interfaces.RSAPublicKey;
import java.util.Base64;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.TimeoutException;
import javax.xml.parsers.ParserConfigurationException;
import org.xml.sax.SAXException;
import org.xml.sax.SAXNotRecognizedException;
import org.xml.sax.SAXNotSupportedException;
import org.xml.sax.helpers.DefaultHandler;

@RetryOnFailure(
    attempts = Tv.SEVEN,
    delay = 1,
    unit = TimeUnit.MINUTES,
    verbose = false,
    types = IOException.class
)
protected Session session() throws IOException {
    try {
        File file = Files.createTempFile("jcabi-ssh", ".key").toFile();
        try (OutputStream os = new FileOutputStream(file)) {
            KeyPair keyPair = KeyGen.rsa(2048);
            RSAPublicKey publicKey = (RSAPublicKey) keyPair.getPublic();
            RSAPrivateKey privateKey = (RSAPrivateKey) keyPair.getPrivate();
            String publicKeyString = Base64.getEncoder().encodeToString(publicKey.getEncoded());
            String privateKeyString = Base6