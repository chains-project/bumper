```java
  @Override
        public Slice slice(final String action) {
            final var permissions = new Permissions.Single(TestAuthentication.ALICE.name(), action);
            final var auth = new BearerAuthScheme(
                token -> CompletableFuture.completedFuture(
                    Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB)
                        .filter(user -> token.equals(token(user)))
                        .map(user -> new Authentication.User(user.name()))
                        .findFirst()
                ),
                ""
            );
            final var astoDocker = new AstoDocker(new InMemoryStorage());
            return new DockerSlice(astoDocker, permissions, auth);
        }
```