```java
public Slice slice(final String action) {
    Authentication.User user = CompletableFuture.completedFuture(
        Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB)
            .filter(u -> token(u).equals(token))
            .map(u -> new Authentication.User(u.name()))
            .findFirst()
    ).join();
    return new DockerSlice(
        new AstoDocker(new InMemoryStorage()),
        new Permissions.Single(TestAuthentication.ALICE.name(), action),
        new BearerAuthScheme(
            t -> CompletableFuture.completedFuture(user),
            ""
        )
    );
}
```