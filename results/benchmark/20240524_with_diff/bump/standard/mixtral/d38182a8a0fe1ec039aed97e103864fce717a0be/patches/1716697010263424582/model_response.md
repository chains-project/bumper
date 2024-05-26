Here's a possible patch for the failing code:
```java
@Override
public Slice slice(String action) {
    return new DockerSlice(new AstoDocker(new InMemoryStorage()), new Authentication.Single(new AuthUser(TestAuthentication.ALICE.name(), ""), action), new BearerAuthScheme((token) -> CompletableFuture.completedFuture(Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB).filter((user) -> token.equals(token(user))).map((user) -> new AuthUser(user.name(), "")).findFirst()), ""));
}
```
The changes made are:

* Importing the new `AuthUser` class and its constructor.
* Replacing the deprecated `Authentication.Single` constructor with the new one that takes an `AuthUser` object.
* Replacing the deprecated `Authentication.User` constructor with the new `AuthUser` constructor.
* Updating the lambda expression in `BearerAuthScheme` constructor to use the new `AuthUser` class.

Note that I had to make some assumptions about the missing imports and the `token` method, since they were not provided in the original code. You might need to adjust them accordingly.