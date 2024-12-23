Here is a patch that should fix the error:
```java
import static java.util.concurrent.TimeUnit.*;

// ...

@java.lang.Override
@com.jcabi.aspects.RetryOnFailure(attempts = 7, delay = 1, unit = MINUTES, verbose = false, types = java.io.IOException.class)
protected com.jcraft.jsch.Session session() throws java.io.IOException {
    try {
        com.jcraft.jsch.JSch.setLogger(new com.jcabi.ssh.JschLogger());
        final com.jcraft.jsch.JSch jsch = new com.jcraft.jsch.JSch();
        com.jcabi.log.Logger.debug(this, "Opening SSH session to %s@%s:%s (auth with password)...", this.getLogin(), this.getAddr(), this.getPort());
        final com.jcraft.jsch.Session session = jsch.getSession(this.getLogin(), this.getAddr(), this.getPort());
        session.setConfig("StrictHostKeyChecking", "no");
        session.setPassword(this.password);
        session.setServerAliveInterval((int) SECONDS.toMillis(10));
        session.setServerAliveCountMax(1000000);
        session.connect((int) SECONDS.toMillis(10));
        return session;
    } catch (final com.jcraft.jsch.JSchException ex) {
        throw new java.io.IOException(ex);
    }
}
```
The changes I made are:

* I imported the `TimeUnit` class and renamed the `Tv` class to it.
* I changed the `Tv.SEVEN` constant to `7`.
* I changed the `Tv.TEN` constant to `10`.
* I changed the `Tv.MILLION` constant to `1000000`.

These changes remove the dependency on the `Tv` class and replace it with standard Java classes and constants.