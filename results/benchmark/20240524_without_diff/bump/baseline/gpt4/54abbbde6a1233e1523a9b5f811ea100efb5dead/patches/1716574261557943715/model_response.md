```java
    // @checkstyle ProtectedMethodInFinalClassCheck (10 lines)
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
            return this.connect(jsch);
        } catch (final JSchException ex) {
            throw new IOException(ex);
        } finally {
            Files.deleteIfExists(file.toPath());
        }
    }
```