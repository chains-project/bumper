```java
protected Session session() throws IOException {
    try {
        JSch.setLogger(new JschLogger());
        final JSch jsch = new JSch();
        Logger.debug(
            this,
            "Opening SSH session to %s@%s:%s (auth with password)...",
            this.getLogin(), this.getAddr(), this.getPort()
        );
        final Session session = jsch.getSession(
            this.getLogin(), this.getAddr(), this.getPort()
        );
        session.setConfig("StrictHostKeyChecking", "no");
        session.setPassword(this.password);
        session.setServerAliveInterval(10 * 60 * 1000);
        session.setServerAliveCountMax(1000000);
        session.connect(10 * 1000);
        return session;
    } catch (final JSchException ex) {
        throw new IOException(ex);
    }
}
```