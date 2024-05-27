Here's the updated `slice` method that uses the new `AuthUser` class from the updated library:

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
                    .map(user -> new AuthUser(user.name(), ""))
                    .findFirst()
            ),
            ""
        )
    );
}
```

Note that I changed the following:

* Imported the new `AuthUser` class from the updated library.
* Replaced the `User` class with `AuthUser` in the `BearerAuthScheme` constructor.
* Added an empty string as the second argument to the `AuthUser` constructor since it now requires two arguments.

I hope this helps! Let me know if you have any questions.