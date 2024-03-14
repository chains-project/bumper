```java
@Override
@RetryOnFailure(
    attempts = 7,
    delay = 1,
    unit = TimeUnit.MINUTES,
    verbose = false,
    types = IOException.class
)
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
        ).value();
        jsch.setHostKeyRepository(new EasyRepo());
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
The error message indicates that the symbol `Tv` can't be found. This is likely due to the fact that the `Tv` class or constant has been removed in the new library version. In this case, `Tv.SEVEN` is used to indicate the number of retry attempts. The simplest fix is to replace `Tv.SEVEN` with the integer `7`.