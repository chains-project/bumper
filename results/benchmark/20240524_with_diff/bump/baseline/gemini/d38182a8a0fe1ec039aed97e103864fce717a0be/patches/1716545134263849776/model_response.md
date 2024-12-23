```java
  @Override
        public Slice slice(final String action) {
            return new DockerSlice(
                new AstoDocker(new InMemoryStorage()),
                new Permissions.Single(TestAuthentication.ALICE.name(), action),
                new BearerAuthScheme(
                    token -> CompletableFuture.completedFuture(
                        Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB)
                            .filter(user -> token.equals(token(user)))
                            .map(user -> new AuthUser(user.name(), user.getPermissions().implies(action) ? Collections.singleton("admin") : Collections.emptySet()))
                            .findFirst()
                    ),
                    ""
                )
            );
        }
```