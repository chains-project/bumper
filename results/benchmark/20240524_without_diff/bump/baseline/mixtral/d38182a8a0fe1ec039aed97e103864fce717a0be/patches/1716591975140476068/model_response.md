Here is a possible patch for the failing client code:
```java
@Override
public Slice slice(final String action) {
    AuthenticationScheme authScheme = new BearerAuthScheme(
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
I created a variable `authScheme` to store the `BearerAuthScheme` instance, and then passed it as an argument to the `DockerSlice` constructor. This way, the code should compile without any issues.