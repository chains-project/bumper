```java
  @Override
        public Slice slice(final String action) {
            final var storage = new InMemoryStorage();
            final var docker = new AstoDocker(storage);
            final var permissions = new Permissions.Single(TestAuthentication.ALICE.name(), action);
            final var authScheme = new BearerAuthScheme(
                token -> CompletableFuture.completedFuture(
                    Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB)
                        .filter(user -> token.equals(token(user)))
                        .map(user -> new Authentication.User(user.name()))
                        .findFirst()
                ),
                ""
            );
            return new DockerSlice(docker, permissions, authScheme);
        }
```