```java
  @Override
        public Slice slice(final String action) {
            final String token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhbGljZSIsImV4cCI6MTY3MjQ4NjY5MX0.654321";
            final BearerAuthScheme authScheme = new BearerAuthScheme(
                    token -> CompletableFuture.completedFuture(
                            Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB)
                                    .filter(user -> token.equals(token(user)))
                                    .map(user -> new Authentication.User(user.name()))
                                    .findFirst()
                    ),
                    ""
            );
            return new DockerSlice(
                new AstoDocker(new InMemoryStorage()),
                new Permissions.Single(TestAuthentication.ALICE.name(), action),
                authScheme
            );
        }
```