Here's the proposed patch for the failing client code:

```java
@Override
public Slice slice(String action) {
    return new DockerSlice(
        new AstoDocker(new InMemoryStorage()),
        new Permissions.Single(TestAuthentication.ALICE.name(), action),
        new BearerAuthScheme(
            token -> CompletableFuture.completedFuture(
                Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB)
                    .filter(user -> token.equals(token(user)))
                    .map(user -> new AuthUser(user.name()))
                    .findFirst()
            ),
            ""
        )
    );
}
```

The changes made are:

* Imported the new `AuthUser` class from the updated library.
* Replaced the `User` class with the new `AuthUser` class.
* Removed the unnecessary import statements for `java.util.stream.Stream` and `java.util.concurrent.CompletableFuture`.
* Removed the explicit reference to the `com.artipie.http` package in the `Permissions.Single` and `BearerAuthScheme` classes.

The rest of the code remains unchanged.