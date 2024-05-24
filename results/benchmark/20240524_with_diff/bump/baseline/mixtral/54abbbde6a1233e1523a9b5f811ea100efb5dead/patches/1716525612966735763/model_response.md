Here's the fixed `session()` method:

```java
protected Session session() throws IOException {
    final File file = File.createTempFile("jcabi-ssh", ".key");
    try {
        JSch.setLogger(new JschLogger());
        final JSch jsch = new JSch();
        new Unchecked<>(
            new LengthOf(
                new TeeInput(
                    this.key.replaceAll("\r", "")
                            .replaceAll("\n\\s+|\n{2,}", "\n")
                            .trim(),
                    file
                )
            )
        )
        .value();
        jsch.setKnownHosts(new EasyRepo());
        if (this.passphrase == null) {
            jsch.addIdentity(file.getAbsolutePath());
        } else {
            jsch.addIdentity(
                this.getLogin(),
                this.key.getBytes(StandardCharsets.UTF_8),
                null,
                this.passphrase.getBytes(StandardCharsets.UTF_8)
            );
        }
        Logger.debug(
            this,
            "Opening SSH session to %s@%s:%s (%d bytes in RSA key)...",
            this.getLogin(), this.getAddr(), this.getPort(),
            file.length()
        );
        return this.session(jsch);
    } catch (final JSchException ex) {
        throw new IOException(ex);
    } finally {
        Files.deleteIfExists(file.toPath());
    }
}
```

The change is in this line:
`jsch.setHostKeyRepository(new EasyRepo());`

It is changed to:
`jsch.setKnownHosts(new EasyRepo());`

`setHostKeyRepository` is removed and replaced with `setKnownHosts` because the former is no longer available in the new version of the library.