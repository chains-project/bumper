```java
  public Slice slice(final String action) {
            final AuthenticationToken token = new BearerAuthScheme("", "").token(TestAuthentication.ALICE.name());
            return new DockerSlice(
                new AstoDocker(new InMemoryStorage()),
                new Permissions.Single(TestAuthentication.ALICE.name(), action),
                new BearerAuthScheme(
                    token1 -> CompletableFuture.completedFuture(
                        Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB)
                            .filter(user -> token1.equals(token))
                            .map(user -> new Authentication.User(user.name()))
                            .findFirst()
                    ),
                    ""
                )
            );
        }
```