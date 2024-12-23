Here's the updated code that replaces the use of the `Tv` class with explicit integer literals, fixing the compilation error:

```java
@Override
@com.jcabi.aspects.RetryOnFailure(attempts = 7, delay = 1, unit = java.util.concurrent.TimeUnit.MINUTES, verbose = false, types = java.io.IOException.class)
protected com.jcraft.jsch.Session session() throws java.io.IOException {
    try {
        com.jcraft.jsch.JSch.setLogger(new com.jcabi.ssh.JschLogger());
        final com.jcraft.jsch.JSch jsch = new com.jcraft.jsch.JSch();
        com.jcabi.log.Logger.debug(this, "Opening SSH session to %s@%s:%s (auth with password)...", this.getLogin(), this.getAddr(), this.getPort());
        final com.jcraft.jsch.Session session = jsch.getSession(this.getLogin(), this.getAddr(), this.getPort());
        session.setConfig("StrictHostKeyChecking", "no");
        session.setPassword(this.password);
        session.setServerAliveInterval(10 * 1000); // was: java.util.concurrent.TimeUnit.SECONDS.toMillis(Tv.TEN)
        session.setServerAliveCountMax(1000000); // was: Tv.MILLION
        session.connect(10 * 1000); // was: java.util.concurrent.TimeUnit.SECONDS.toMillis(10L)
        return session;
    } catch (final com.jcraft.jsch.JSchException ex) {
        throw new java.io.IOException(ex);
    }
}
```

The changes include:

* Replacing the `Tv.SEVEN` constant with the explicit integer `7` for the `attempts` parameter of the `@RetryOnFailure` annotation.
* Replacing the `Tv.TEN` constant with the explicit integer `10` for the `ServerAliveInterval` and `connect` methods of the `Session` object.
* Replacing the `Tv.MILLION` constant with the explicit integer `1000000` for the `ServerAliveCountMax` method of the `Session` object.
* Removing the `java.util.concurrent.TimeUnit.SECONDS.toMillis` method calls, since the explicit integer literals are already in milliseconds.