Here is a proposed patch for the failing client code:
```java
import static java.util.concurrent.TimeUnit.MINUTES;
import static java.util.concurrent.TimeUnit.SECONDS;

// ...

@Override
@com.jcabi.aspects.RetryOnFailure(attempts = 7, delay = 1, unit = MINUTES, verbose = false, types = IOException.class)
protected com.jcraft.jsch.Session session() throws java.io.IOException {
    try {
        com.jcraft.jsch.JSch.setLogger(new com.jcabi.ssh.JschLogger());
        final com.jcraft.jsch.JSch jsch = new com.jcraft.jsch.JSch();
        com.jcabi.log.Logger.debug(this, "Opening SSH session to %s@%s:%s (auth with password)...", this.getLogin(), this.getAddr(), this.getPort());
        final com.jcraft.jsch.Session session = jsch.getSession(this.getLogin(), this.getAddr(), this.getPort());
        session.setConfig("StrictHostKeyChecking", "no");
        session.setPassword(this.password);
        long tenSeconds = SECONDS.toMillis(10);
        session.setServerAliveInterval(tenSeconds);
        session.setServerAliveCountMax(1_000_000);
        session.connect((int) tenSeconds);
        return session;
    } catch (final com.jcraft.jsch.JSchException ex) {
        throw new java.io.IOException(ex);
    }
}
```
I have replaced the references to the removed `Tv` class with the equivalent constant values from the `java.util.concurrent.TimeUnit` class. I have also created a new variable `tenSeconds` to store the number of milliseconds in 10 seconds, to make the code easier to read.