Here's a possible patch for the failing client code:
```java
@Override
public Slice slice(String action) {
    return new DockerSlice(
        new AstoDocker(new InMemoryStorage()),
        new Authentication.Single(new AuthUser(TestAuthentication.ALICE.name(), action), action),
        new BearerAuthScheme(
            token -> CompletableFuture.completedFuture(
                Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB)
                    .filter(user -> token.equals(token(user)))
                    .map(user -> new AuthUser(user.name()))
                    .findFirst()),
            ""
        )
    );
}
```
I changed the following:

* Imported `com.artipie.http.auth.AuthUser` instead of `com.artipie.http.auth.Authentication.User`.
* Changed `new Authentication.Single(TestAuthentication.ALICE.name(), action)` to `new Authentication.Single(new AuthUser(TestAuthentication.ALICE.name(), action), action)`.

This should fix the compilation error you were seeing. Note that there might be other ways to fix the error, but this is one possible solution.