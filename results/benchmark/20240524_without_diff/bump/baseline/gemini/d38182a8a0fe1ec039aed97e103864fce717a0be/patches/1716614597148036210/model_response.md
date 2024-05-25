```java
  @Override
        public Slice slice(final String action) {
            final Authentication.User user = new Authentication.User(TestAuthentication.ALICE.name());
            final Permissions permissions = new Permissions.Single(user.getName(), action);
            return new DockerSlice(
                new AstoDocker(new InMemoryStorage()),
                permissions,
                new BearerAuthScheme(
                    token -> CompletableFuture.completedFuture(
                        Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB)
                            .filter(u -> token.equals(token(u)))
                            .map(Authentication.User::new)
                            .findFirst()
                    ),
                    ""
                )
            );
        }
```