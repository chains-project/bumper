```java
  @Override
        public Slice slice(final String action) {
            // Create a new BearerAuthScheme instance with the provided token validation logic.
            final BearerAuthScheme authScheme = new BearerAuthScheme(
                token -> CompletableFuture.completedFuture(
                    Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB)
                        .filter(user -> token.equals(token(user)))
                        .map(user -> new Authentication.User(user.name()))
                        .findFirst()
                ),
                ""
            );

            // Create a new DockerSlice instance using the provided AstoDocker, permissions, and auth scheme.
            return new DockerSlice(
                new AstoDocker(new InMemoryStorage()),
                new Permissions.Single(TestAuthentication.ALICE.name(), action),
                authScheme
            );
        }
```