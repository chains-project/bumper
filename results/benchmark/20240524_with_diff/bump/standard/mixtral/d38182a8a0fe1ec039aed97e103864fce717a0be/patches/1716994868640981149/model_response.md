Here's the proposed patch for the failing client code:
```java
@Override
public Slice slice(String action) {
    return new DockerSlice(new AstoDocker(new InMemoryStorage()), new Authentication.Single(new AuthUser(TestAuthentication.ALICE.name(), action), action), new BearerAuthScheme((token) -> CompletableFuture.completedFuture(Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB)
            .filter((user) -> token.equals(token(user)))
            .map((user) -> new AuthUser(user.name()))
            .collect(Collectors.toList())), ""));
}
```
The changes made include:

* Importing the new `AuthUser` class from `com.artipie.http.auth` package.
* Replacing the deprecated `Authentication.Single` constructor with the new one that takes `AuthUser` instead of `Authentication.User`.
* Updating the lambda expression in `BearerAuthScheme` constructor to return a list of `AuthUser` objects instead of `Authentication.User`.

Note that I had to make some assumptions about the imports and the missing classes, so you might need to adjust the code accordingly.