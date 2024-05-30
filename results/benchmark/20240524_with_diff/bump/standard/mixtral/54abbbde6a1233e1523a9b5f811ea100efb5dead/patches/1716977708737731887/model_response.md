Here's a suggested patch for the code that replaces the usage of `Tv` with explicit values:

```java
@java.lang.Override
@com.jcabi.aspects.RetryOnFailure(attempts = 7, delay = 1, unit = java.util.concurrent.TimeUnit.MINUTES, verbose = false, types = java.io.IOException.class)
protected com.jcraft.jsch.Session session() throws java.io.IOException {
    try {
        com.jcraft.jsch.JSch.setLogger(new com.jcabi.ssh.JschLogger());
        final com.jcraft.jsch.JSch jsch = new com.jcraft.jsch.JSch();
        com.jcabi.log.Logger.debug(this, "Opening SSH session to %s@%s:%s (auth with password)...", this.getLogin(), this.getAddr(), this.getPort());
        final com.jcraft.jsch.Session session = jsch.getSession(this.getLogin(), this.getAddr(), this.getPort());
        session.setConfig("StrictHostKeyChecking", "no");
        session.setPassword(this.password);
        session.setServerAliveInterval(10 * 1000); // was: Tv.TEN
        session.setServerAliveCountMax(1000000);   // was: Tv.MILLION
        session.connect(10 * 1000);                 // was: Tv.TEN
        return session;
    } catch (final com.jcraft.jsch.JSchException ex) {
        throw new java.io.IOException(ex);
    }
}
```

This patch replaces the usage of `Tv.TEN` and `Tv.MILLION` with explicit values of `10 * 1000` and `1000000`, respectively. This should resolve the "cannot find symbol" error caused by the missing `Tv` symbol.