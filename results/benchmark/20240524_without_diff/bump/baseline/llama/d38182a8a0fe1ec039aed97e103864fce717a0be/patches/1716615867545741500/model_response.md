```
public Slice slice(final String action) {
    Authentication.User user = Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB)
        .filter(u -> token(u).equals(token(u)))
        .map(u -> new Authentication.User(u.name()))
        .findFirst()
        .orElseThrow();
    return new DockerSlice(
        new AstoDocker(new InMemoryStorage()),
        new Permissions.Single(user.getName(), action),
        new BearerAuthScheme(
            token -> CompletableFuture.completedFuture(user),
            ""
        )
    );
}
```