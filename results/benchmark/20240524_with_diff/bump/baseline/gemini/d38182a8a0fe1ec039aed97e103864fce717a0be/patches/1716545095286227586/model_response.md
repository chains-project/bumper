```java
  public Slice slice(final String action) {
    final var authUser = new AuthUser(TestAuthentication.ALICE.name(), "");
    return new DockerSlice(
        new AstoDocker(new InMemoryStorage()),
        new Permissions.Single(authUser, action),
        new BearerAuthScheme(
            token -> CompletableFuture.completedFuture(
                Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB)
                    .filter(user -> token.equals(token(user)))
                    .map(user -> new AuthUser(user.name(), ""))
                    .findFirst()
            ),
            ""
        )
    );
}
```