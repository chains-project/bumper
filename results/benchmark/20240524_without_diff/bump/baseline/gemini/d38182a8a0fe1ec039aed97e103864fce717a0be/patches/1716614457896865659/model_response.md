```java
  @Override
        public Slice slice(final String action) {
            final AstoDocker astoDocker = new AstoDocker(new InMemoryStorage());
            final Permissions.Single permissions = new Permissions.Single(TestAuthentication.ALICE.name(), action);
            final BearerAuthScheme bearerAuthScheme = new BearerAuthScheme(
                token -> CompletableFuture.completedFuture(
                    Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB)
                        .filter(user -> token.equals(token(user)))
                        .map(user -> new Authentication.User(user.name()))
                        .findFirst()
                ),
                ""
            );
            return new DockerSlice(astoDocker, permissions, bearerAuthScheme);
        }
```