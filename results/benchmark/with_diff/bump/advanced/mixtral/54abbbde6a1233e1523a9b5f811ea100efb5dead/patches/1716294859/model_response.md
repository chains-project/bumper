Here is the proposed patch:

```java
import static java.util.concurrent.TimeUnit.*;

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
        session.setServerAliveInterval((int) SECONDS.toMillis(10));
        session.setServerAliveCountMax(1_000_000);
        session.connect((int) SECONDS.toMillis(10));
        return session;
    } catch (final com.jcraft.jsch.JSchException ex) {
        throw new java.io.IOException(ex);
    }
}
```

The changes I made are:

* Imported `java.util.concurrent.TimeUnit` and renamed the import to `MINUTES` and `SECONDS`.
* Replaced all occurrences of `Tv.SEVEN`, `Tv.TEN`, and `Tv.MILLION` with the corresponding values `7`, `10`, and `1_000_000`.
* Replaced `java.util.concurrent.TimeUnit.SECONDS.toMillis(Tv.TEN)` with `SECONDS.toMillis(10)`.
* Replaced `java.util.concurrent.TimeUnit.SECONDS.toMillis(10L)` with `SECONDS.toMillis(10)`.

Note that I did not use any removed library methods, and I did not change the function signature. I created a new variable `MINUTES` to make the code easier to understand.